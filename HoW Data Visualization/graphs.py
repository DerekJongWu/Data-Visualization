import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

def total_graph(filename):
    df = pd.read_excel(filename)
    data= df.iloc[:14]
    data = data.drop(columns = 'Unnamed: 0')
    data = data.drop(columns = "Unnamed: 9")
    data.rename(columns={'YTD ORDER SUMMARY':'month'}, inplace=True)
    data.rename(columns={'Unnamed: 2':'2019_Qty'}, inplace=True)
    data.rename(columns={'Unnamed: 3':'2019_$'}, inplace=True)
    data.rename(columns={'Unnamed: 4':'2018_Qty'}, inplace=True)
    data.rename(columns={'Unnamed: 5':'2018_$'}, inplace=True)
    data.rename(columns={'Unnamed: 6':'diff_Qty'}, inplace=True)
    data.rename(columns={'Unnamed: 7':'diff_$'}, inplace=True)
    data.rename(columns={'Unnamed: 8':'%diff_$'}, inplace=True)
    data = data.drop([0,1,2,3,11,12,13])
    ax = data.plot(x='month', y='2019_Qty', rot = '0', kind= 'bar', figsize=(7, 7))
    ax.set_xlabel("Month")
    ax.set_ylabel("Qty Sold")
    ax.set_title('Total Quantity Sold by Month')
    plt.savefig("Total.jpg")

def state_graphs(filename, num_states):
    df = pd.read_excel(filename)
    column = 16 
    for i in range (num_states): 
        state_data= df.iloc[column:column+7]
        state_data.rename(columns={'Unnamed: 2':'Month'}, inplace=True)
        state_data.rename(columns={'Unnamed: 3':'2019_Qty'}, inplace=True)
        state_data.rename(columns={'Unnamed: 4':'2019_$'}, inplace=True)
        state_data.rename(columns={'Unnamed: 5':'2018_Qty'}, inplace=True)
        state_data.rename(columns={'Unnamed: 6':'2018_$'}, inplace=True)
        state_data.rename(columns={'Unnamed: 7':'diff_Qty'}, inplace=True)
        state_data.rename(columns={'Unnamed: 8':'diff_$'}, inplace=True)
        state_data.rename(columns={'Unnamed: 9':'%diff_$'}, inplace=True)
        state_data = state_data.drop(columns = 'Unnamed: 0')
        state_name = state_data['YTD ORDER SUMMARY'].iloc[0]
        ax = state_data.plot(kind='bar', x = 'Month', y = {'2019_$', '2018_$'}, rot = '0', figsize = (7,7))
        ax.set_xlabel("Month")
        ax.set_ylabel("$ Sold")
        ax.set_title(state_name + " $ by Month")
        plt.savefig(state_name + ".jpg")
        column = column + 8 

filename = sys.argv[1]
num_states = int(sys.argv[2])

total_graph(filename)
state_graphs(filename, num_states)
