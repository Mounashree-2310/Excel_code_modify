import pandas as pd


def test_ticket_null_replacement():
    df = pd.DataFrame({"TICKET": [None]})

    df["TICKET"] = df["TICKET"].fillna("NULL")

    assert df["TICKET"][0] == "NULL"


def test_irregular_failure_filter():
    df = pd.DataFrame(
        {
            "CATEGORY": [
                "IRREGULAR_TEST_FAILURE",
                "REGULAR_TEST_FAILURE",
                "IRREGULAR_TEST_FAILURE",
            ]
        }
    )

    filtered_df = df[
        df["CATEGORY"] == "IRREGULAR_TEST_FAILURE"
    ]

    assert len(filtered_df) == 2
