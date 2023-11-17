import pandas as pd
import matplotlib.pyplot as plt


def solution_7a(imp_df):
    "Find the volume (forecast & actual) that each DC processes in a week"
    # grouping and adding columns actual_qty and fcst_qty on the dataframe on dc_id and acct_wk_i
    gk=imp_df.groupby(['dc_id','acct_wk_i'])[['actual_qty','fcst_qty']].sum().reset_index()
    print(gk)

def solution_7b(imp_df):
    " Calculate the share in % terms of each DC with respect to all DCs in a week"
    gk=imp_df.groupby(['dc_id','acct_wk_i'])[['actual_qty','fcst_qty']].sum().reset_index()
    # getting the percentage share  
    gk['actual_percentage_share']=gk.groupby('acct_wk_i')['actual_qty'].transform(lambda x: (x / x.sum()) * 100)
    gk['forecast_percentage_share']=gk.groupby('acct_wk_i')['fcst_qty'].transform(lambda x: (x / x.sum()) * 100)
    print( gk)


def solution_7c(imp_df):
    "Plot a trend chart of this share for each DC"
    gk=imp_df.groupby(['dc_id','acct_wk_i'])[['actual_qty','fcst_qty']].sum().reset_index()
    gk['actual_percentage_share']=gk.groupby('acct_wk_i')['actual_qty'].transform(lambda x: (x / x.sum()) * 100)

    for dc_id in gk['dc_id'].unique():
        df_dc_id = gk[gk['dc_id'] == dc_id]
        plt.plot(df_dc_id['acct_wk_i'], df_dc_id['actual_qty'], label=dc_id)

    
    plt.xlabel('Week')
    plt.ylabel('Quantity')
    plt.title('Trend Chart for Quantity by DC ID')
    plt.legend()
    plt.show()




if __name__=="__main__":

    df = pd.read_excel("S&OP_Assessment_Test.xlsx", sheet_name='Table A')
    imp_df=df[['dc_id','actual_qty','fcst_qty','acct_wk_i']]

    print(" Volume tha each DC processes in a week")
    solution_7a(imp_df)

    print(" Calculate the share in % terms of each DC with respect to all DCs in a week")
    solution_7b(imp_df)
    
    print("Plot a trend chart of this share for each DC")
    solution_7c(imp_df)