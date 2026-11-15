# KYC Document Checker

A small Streamlit demo for reviewing fictional customer onboarding records. Python rules check for an identity document, proof of address, and a name match across the application form and identity document. Each result includes its source and the evidence used. A flagged check sends the case to manual review.

The app uses built-in synthetic records and runs without an API key. It checks the supplied fields in those records. Document authenticity and identity verification are outside the scope of this demo.

## Run on Windows

Install standard Windows Python 3.12 or 3.13 from [python.org](https://www.python.org/downloads/windows/). Open PowerShell and run the following commands from the project folder. Update the path if you saved the project elsewhere.

```powershell
Set-Location 'E:\kyc-document-checker'
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

If the browser does not open automatically, visit [localhost:8501](http://localhost:8501). Press `Ctrl+C` in PowerShell to stop the app. If `py` is unavailable, use `python -m venv .venv` with a standard Windows Python installation that includes pip.

## Try the sample cases

Select a case and click **Run check**.

| Sample case | Expected flagged check | Manual review |
| --- | --- | --- |
| Complete documents | None | No |
| Missing proof of address | Proof of address present | Yes |
| Name mismatch | Name matches | Yes |

## Change the rules

- Edit `run_checks()` in `checker.py` to change the checks. The name comparison trims surrounding whitespace and ignores case.
- Edit `CASES` in `checker.py` to change the sample data. Use `None` for a missing document field.
- Edit the `any(...)` condition in `app.py` to change when a case requires manual review.
