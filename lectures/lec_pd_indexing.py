# Outline꞉
# 1. Selection using .loc ﴾label based﴿
# 1.1 Series꞉
# 1.1.1 Selection using a single label
# 1.1.2 Selection using sequence of labels
# 1.1.3 Selection using slices
# 1.2 DataFrame꞉
# 1.2.1 Selection using a single label
# 1.2.2 Selection using sequence of labels
# 1.2.3 Selection using slices
# 2. Selection using .iloc ﴾position based﴿
# 2.1 Series꞉
# 2.1.1 Selection using a single label
# 2.1.2 Selection using sequence of labels
# 2.1.3 Selection using slices
# 2.2 DataFrame꞉
# 2.2.1 Selection using a single label
# 2.2.2 Selection using sequence of labels
# 2.2.3 Selection using slices
# 3. Selection using []
# 3.1 Series꞉
# 3.1.1 label, list of labels, label slices
# 3.1.2 position, list of positions, position slices
# 3.2 DataFrame꞉
# 3.2.1 column label, list of column labels
# 3.2.2 row label slices
# 3.2.3 row position slices
import pandas as pd
ser = pd.Series(data=prices, index=dates)
print(ser)
