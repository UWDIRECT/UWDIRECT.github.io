import pandas as pd

import pc

def test_row_i_to_row_j():
    df = pd.DataFrame([[-1, 0, 1], [1, 0, -1], [.5, 0, .5]])
    A = df.loc[0]
    B = df.loc[1]
    C = df.loc[2]
    assert int(pc.row_i_to_row_j(A, A)) == 1, "Diagonal elements not handled properly"
    assert int(pc.row_i_to_row_j(A, B)) == -1, "Anticorrelated elements not handled properly"
    assert int(pc.row_i_to_row_j(A, C)) == 0, "Uncorrelated elements not handled properly"
    return
