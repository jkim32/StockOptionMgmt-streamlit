import os
import streamlit as st
import pandas as pd
@st.cache_data
def app():
    st.title('Show All')
    if 'df_dict' not in st.session_state:
        # 현재 디렉토리 경로 가져오기
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_name = 'Stock Option DB Sample.xlsx'
        excel_file = os.path.join(current_dir, file_name)

        
        # 엑셀 파일의 모든 시트를 DataFrame으로 불러오기
        st.session_state.df_dict = pd.read_excel(excel_file, sheet_name=None)
    # st.write(st.session_state.df_dict)
    for sheet_name, df in st.session_state.df_dict.items():
        st.write(sheet_name)
        st.dataframe(df)

if __name__ == "__main__":
    app()

