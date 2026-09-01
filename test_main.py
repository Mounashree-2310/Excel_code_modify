import pandas as pd


def test_ticket_null_replacement():
    df = pd.DataFrame(
        {
            "TICKET": [None]
        }
    )

    df["TICKET"] = (
        df["TICKET"]
        .fillna("NULL")
    )

    assert df["TICKET"][0] == "NULL"
    
