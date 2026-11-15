import streamlit as st

from checker import CASES, run_checks


st.set_page_config(page_title="KYC Document Checker")
st.title("KYC Document Checker")
st.caption("Onboarding document review using fictional customer data.")

with st.form("review"):
    selected_case = st.selectbox("Sample case", list(CASES))
    submitted = st.form_submit_button("Run check", type="primary")

if submitted:
    results = run_checks(CASES[selected_case])
    st.subheader(selected_case)

    if any(not result.passed for result in results):
        st.warning("Manual review required")
    else:
        st.success("Manual review not required")

    st.table([
        {
            "Check": result.check,
            "Result": "Pass" if result.passed else "Flagged",
            "Source": result.source,
            "Evidence": result.details,
        }
        for result in results
    ])
