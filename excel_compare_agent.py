import pandas as pd
import streamlit as st

st.set_page_config(page_title="Excel Comparison Agent", layout="wide")
st.title("Free Excel Comparison Agent")

file1 = st.file_uploader("Upload Excel File 1", type=["xlsx"])
file2 = st.file_uploader("Upload Excel File 2", type=["xlsx"])

key_column = st.text_input("Enter Unique ID Column Name")

if file1 and file2 and key_column:
    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)

    if key_column not in df1.columns or key_column not in df2.columns:
        st.error("Unique ID column not found in both files")
    else:
        merged = df1.merge(
            df2,
            on=key_column,
            how="outer",
            suffixes=("_old", "_new"),
            indicator=True
        )

        diff_rows = []

        for _, row in merged.iterrows():
            if row["_merge"] != "both":
                diff_rows.append(row)
            else:
                for col in df1.columns:
                    if col != key_column:
                        if row[f"{col}_old"] != row[f"{col}_new"]:
                            diff_rows.append(row)
                            break

        diff_df = pd.DataFrame(diff_rows)

        st.dataframe(diff_df)

        st.download_button(
            "Download Difference Report",
            diff_df.to_excel(index=False, engine="openpyxl"),
            "difference_report.xlsx"
        )
