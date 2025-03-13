import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

def draw_plot():
    # 1️⃣ Load Data
    df = pd.read_csv("epa-sea-level.csv")

    # 2️⃣ Buat Scatter Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Data", color="blue")

    # 3️⃣ Regresi Linear (1880-2050)
    slope, intercept, _, _, _ = stats.linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_extended = range(1880, 2051)
    sea_levels_extended = intercept + slope * pd.Series(years_extended)
    ax.plot(years_extended, sea_levels_extended, color="red", label="Best Fit (1880-2050)")

    # 4️⃣ Regresi Linear (2000-2050)
    df_recent = df[df["Year"] >= 2000]
    slope_recent, intercept_recent, _, _, _ = stats.linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    years_recent = range(2000, 2051)
    sea_levels_recent = intercept_recent + slope_recent * pd.Series(years_recent)
    ax.plot(years_recent, sea_levels_recent, color="green", linestyle="dashed", label="Best Fit (2000-2050)")

    # 5️⃣ Tambahkan Label dan Judul
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.legend()

    # 6️⃣ Simpan Gambar
    fig.savefig("sea_level_plot.png")

    return fig  # ✅ Kembalikan hanya `fig`
