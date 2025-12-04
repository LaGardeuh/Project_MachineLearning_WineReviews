import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
from geopy.geocoders import Nominatim

def run():
    file_cleaned_path = "./data/cleaned/wine_data_cleaned.csv"
    df = pd.read_csv(file_cleaned_path)

    st.write("""
    # App web
    """)

    st.write(df.head())
    st.write(df.describe())

    # Titre
    st.subheader("Analyse des valeurs aberrantes (Outliers)")

    # Créer les boxplots
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    sns.boxplot(data=df, y='price', ax=axes[0])
    axes[0].set_title('Distribution des prix')

    sns.boxplot(data=df, y='points', ax=axes[1])
    axes[1].set_title('Distribution des points')

    plt.tight_layout()

    # Afficher dans Streamlit
    st.pyplot(fig)

    # Analyser les outliers numériquement
    st.subheader("Analyse quantitative des outliers")

    # Pour price
    Q1_price = df['price'].quantile(0.25)
    Q3_price = df['price'].quantile(0.75)
    IQR_price = Q3_price - Q1_price
    lower_bound_price = Q1_price - 1.5 * IQR_price
    upper_bound_price = Q3_price + 1.5 * IQR_price

    outliers_price = df[(df['price'] < lower_bound_price) |
                        (df['price'] > upper_bound_price)]

    # Afficher les stats pour price
    st.write("**PRICE:**")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Q1", f"{Q1_price:.2f}€")
        st.metric("Q3", f"{Q3_price:.2f}€")
    with col2:
        st.metric("IQR", f"{IQR_price:.2f}€")
        st.metric("Bornes (en €)", f"[{lower_bound_price:.2f}, {upper_bound_price:.2f}]")
    with col3:
        st.metric("Outliers count", f"{len(outliers_price)} ({len(outliers_price) / len(df) * 100:.2f}%)")
        if len(outliers_price) > 0:
            st.metric("Prix min outlier", f"{outliers_price['price'].min():.2f}€")
            st.metric("Prix max outlier", f"{outliers_price['price'].max():.2f}€")

    st.write("Les bornes outliers sont -22 (en euro donc imposibles) et 90 sauf que nous parlons de bouteilles de vin. Il n'est donc pas aberrant que nous ayons des valeurs pouvant monter jusqu'à plus de 2000 euros.")

    # Pour points
    Q1_points = df['points'].quantile(0.25)
    Q3_points = df['points'].quantile(0.75)
    IQR_points = Q3_points - Q1_points
    lower_bound_points = Q1_points - 1.5 * IQR_points
    upper_bound_points = Q3_points + 1.5 * IQR_points

    outliers_points = df[(df['points'] < lower_bound_points) |
                         (df['points'] > upper_bound_points)]

    # Afficher les stats pour points
    st.write("**POINTS:**")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Q1", f"{Q1_points:.2f}")
        st.metric("Q3", f"{Q3_points:.2f}")
    with col2:
        st.metric("IQR", f"{IQR_points:.2f}")
        st.metric("Bornes", f"[{lower_bound_points:.2f}, {upper_bound_points:.2f}]")
    with col3:
        st.metric("Outliers", f"{len(outliers_points)} ({len(outliers_points) / len(df) * 100:.2f}%)")

    df_map = pd.read_csv('./data/cleaned/wine_data_province_lat_long.csv')
    df_map = df_map.dropna(subset=['latitude', 'longitude'])
    st.map(df_map)



if __name__ == "__main__":
    run()