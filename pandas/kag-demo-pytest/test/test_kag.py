import pytest
import kag


@pytest.fixture(scope='session')
def df():
    df = kag.load_raw('data/kaggle-survey-2018.zip')
    return kag.tweak_kag(df)


def test_salary_mean(df):
    assert 10_000 < df.Salary.mean() < 100_000

def test_salary_between(df):
    assert df.Salary.min() >= 0
    assert df.Salary.max() <= 500_000

def test_salary_not_null(df):
    assert not df.Salary.isna().any()

def test_country_values(df):
    assert set(df.Country.unique()) == {'Another', 'United States of America', 'India', 'China'}

def test_salary_dtype(df):
    assert df.Salary.dtype == int
    
def test_ge(df):
    import json
    import great_expectations as ge
    res = ge.validate(ge.from_pandas(df),
        expectation_suite=json.load(open('kaggle_expectations.json')))
    failures = []
    for exp in res['results']:
        if not exp['success']:
            failures.append(json.dumps(exp, indent=2))
    if failures:
        assert False, '\n'.join(failures)
    else:
        assert True

