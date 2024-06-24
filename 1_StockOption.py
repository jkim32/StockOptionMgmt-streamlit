import streamlit as st
import pandas as pd

def app():
    if 'df_dict' in st.session_state:
        st.title('스톡옵션 현황')
        if '스톡옵션_최신' in st.session_state.df_dict:
            df = st.session_state.df_dict['스톡옵션_최신']
            st.dataframe(df)
        else:
            st.write("'스톡옵션_최신' 시트를 찾을 수 없습니다.")

    else:
        st.write("데이터를 불러오는 중입니다...")

if __name__ == '__main__':
    app()
