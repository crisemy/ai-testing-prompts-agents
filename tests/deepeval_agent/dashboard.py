import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AI Agent QA Dashboard", layout="wide", page_icon="🤖")

st.title("🤖 AI Agent QA Dashboard")
st.markdown("Offline evaluation metrics generated via **DeepEval** and **LangChain**.")

try:
    df = pd.read_csv("eval_results.csv")
    
    # Replace boolean with strings for easier plotting
    df['Success_Str'] = df['Success'].replace({True: 'Pass', False: 'Fail'})
    
    # High-level KPIs
    pass_rate = (df['Success'] == True).mean() * 100
    avg_score = df['Score'].mean()
    
    col1, col2, col3 = st.columns(3)
    col1.metric("📝 Total Tests Ran", len(df))
    col2.metric("✅ Pass Rate", f"{pass_rate:.1f}%")
    col3.metric("🎯 Avg Relevancy Score", f"{avg_score:.2f}")
    
    st.divider()
    
    # Data Visualizations
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Success vs Failure")
        fig = px.pie(
            df, 
            names='Success_Str', 
            color='Success_Str', 
            color_discrete_map={'Pass':'#28a745', 'Fail':'#dc3545'},
            hole=0.4
        )
        st.plotly_chart(fig, use_container_width=True)
        
    with c2:
        st.subheader("Distribution of Scores")
        fig2 = px.histogram(
            df, 
            x='Score', 
            nbins=10, 
            color='Metric Name',
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        st.plotly_chart(fig2, use_container_width=True)
        
    st.divider()
    
    # Detailed Data Table
    st.subheader("Detailed Evaluation Results")
    st.markdown("Review the reasons why specific tests failed below:")
    
    # Styled dataframe
    st.dataframe(
        df[["Input", "Actual Output", "Metric Name", "Score", "Success", "Reason"]], 
        use_container_width=True,
        hide_index=True
    )

except FileNotFoundError:
    st.warning("⚠️ No evaluation results found! Please run `run_evals.py` first to generate the dataset.")
