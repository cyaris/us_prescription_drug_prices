from copy import deepcopy

def drug_name_match(df_1, df_1_col_1, df_1_col_2, df_2, df_2_col):
    for i, df_1_item in enumerate(df_1[df_1_col_2].str.lower()):
        for z, df_2_item in enumerate(df_2[df_2_col].str.lower()):
            if df_1_item in df_2_item:
                df_1.loc[i, df_1_col_1] = df_2[df_1_col_1][z]

def drug_name_filter_match(df_1, df_1_col_1, df_1_col_2, df_2, df_2_col):
    copy_df = deepcopy(df_1)
    for i, df_1_item in enumerate(df_1[df_1[df_1_col_1] == 'No Match'][df_1_col_2].str.lower()):
        for z, df_2_item in enumerate(df_2[df_2_col].str.lower()):
            if df_1_item in df_2_item:
                df_1.loc[copy_df[copy_df[df_1_col_1] == 'No Match'].index[i], df_1_col_1] = df_2[df_1_col_1][z]