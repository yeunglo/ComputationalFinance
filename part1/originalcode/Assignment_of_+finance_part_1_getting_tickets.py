#!python3
# coding: utf-8

# In[2]:


from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
import datetime


# In[3]:


from pandas_datareader import DataReader
from datetime import datetime
import matplotlib.pyplot as plt


# In[38]:


#fetch the FTSE 100 index data from Yahoo
ftse_data = DataReader('^FTSE',  'yahoo', datetime(2015, 2, 20), datetime(2018, 2, 20))
#print(ftse_data['Adj Close'])


# In[51]:


ftse_data.to_csv("./FTSE.csv")


# In[39]:


#fetch the 30 companies data from Yahoo

#Vodafone Group Plc (VOD.L)
VOD_L_data = DataReader('VOD.L',  'yahoo', datetime(2015, 2, 20), datetime(2018, 2, 20))


# In[40]:


'''
plt.figure(figsize=(16,9))
plt.plot(VOD_L_data['Close'])
plt.ylabel('VOD.L 100')
plt.show()
'''


# In[40]:


#Shire plc (SHP.L)
SHP_L_data = DataReader('SHP.L',  'yahoo', datetime(2015, 2, 20), datetime(2018, 2, 20))


# In[41]:


#British American Tobacco p.l.c. (BATS.L)
BATS_L_data = DataReader('BATS.L',  'yahoo', datetime(2015, 2, 20), datetime(2018, 2, 20))


# In[42]:


#Schroders plc (SDR.L)
SDR_L_data = DataReader('SDR.L',  'yahoo', datetime(2015, 2, 20), datetime(2018, 2, 20))


# In[5]:


#RDSA.L	Royal Dutch Shell plc
RDSA_L_data = DataReader('RDSA.L',  'yahoo', datetime(2015, 2, 20), datetime(2018, 2, 20))


# In[6]:


#CPG.L	Compass Group PLC
CPG_L_data = DataReader('CPG.L',  'yahoo', datetime(2015, 2, 20), datetime(2018, 2, 20))


# In[8]:


#CCH.L	Coca-Cola HBC AG
CCH_L_data = DataReader('CCH.L',  'yahoo', datetime(2015, 2, 20), datetime(2018, 2, 20))


# In[9]:


#SMIN.L	Smiths Group plc
SMIN_L_data = DataReader('SMIN.L',  'yahoo', datetime(2015, 2, 20), datetime(2018, 2, 20))


# In[10]:


#SKY.L	Sky plc
SKY_L_data = DataReader('SKY.L',  'yahoo', datetime(2015, 2, 20), datetime(2018, 2, 20))


# In[11]:


#DLG.L	Direct Line Insurance Group PLC
DLG_L_data = DataReader('DLG.L',  'yahoo', datetime(2015, 2, 20), datetime(2018, 2, 20))


# In[12]:


#SSE.L	SSE plc
SSE_L_data = DataReader('SSE.L',  'yahoo', datetime(2015, 2, 20), datetime(2018, 2, 20))


# In[13]:


#NMC.L	NMC Health Plc
NMC_L_data = DataReader('NMC.L',  'yahoo', datetime(2015, 2, 20), datetime(2018, 2, 20))


# In[14]:


#PPB.L	Paddy Power Betfair plc
PPB_L_data = DataReader('PPB.L',  'yahoo', datetime(2015, 2, 20), datetime(2018, 2, 20))


# In[15]:


#ANTO.L	Antofagasta plc
ANTO_L_data = DataReader('ANTO.L',  'yahoo', datetime(2015, 2, 20), datetime(2018, 2, 20))


# In[16]:


#PRU.L	Prudential plc
PRU_L_data = DataReader('PRU.L',  'yahoo', datetime(2015, 2, 20), datetime(2018, 2, 20))


# In[17]:


#STJ.L	St. James's Place plc
STJ_L_data = DataReader('STJ.L',  'yahoo', datetime(2015, 2, 20), datetime(2018, 2, 20))


# In[18]:


#GFS.L	G4S plc
GFS_L_data = DataReader('GFS.L',  'yahoo', datetime(2015, 2, 20), datetime(2018, 2, 20))


# In[19]:


#AHT.L	Ashtead Group plc	
AHT_L_data = DataReader('AHT.L',  'yahoo', datetime(2015, 2, 20), datetime(2018, 2, 20))


# In[20]:


#CCL.L	Carnival plc
CCL_L_data = DataReader('CCL.L',  'yahoo', datetime(2015, 2, 20), datetime(2018, 2, 20))


# In[21]:


#RTO.L	Rentokil Initial plc
RTO_L_data = DataReader('RTO.L',  'yahoo', datetime(2015, 2, 20), datetime(2018, 2, 20))


# In[22]:


#CNA.L	Centrica plc
CNA_L_data = DataReader('CNA.L',  'yahoo', datetime(2015, 2, 20), datetime(2018, 2, 20))


# In[23]:


#EXPN.L	Experian plc
EXPN_L_data = DataReader('EXPN.L',  'yahoo', datetime(2015, 2, 20), datetime(2018, 2, 20))


# In[28]:


#EZJ.L	easyJet plc
EZJ_L_data = DataReader('EZJ.L',  'yahoo', datetime(2015, 2, 20), datetime(2018, 2, 20))


# In[29]:


#SMT.L	Scottish Mortgage Investment Trust PLC
SMT_L_data = DataReader('SMT.L',  'yahoo', datetime(2015, 2, 20), datetime(2018, 2, 20))


# In[30]:


#TUI.L	TUI AG
TUI_L_data = DataReader('TUI.L',  'yahoo', datetime(2015, 2, 20), datetime(2018, 2, 20))


# In[31]:


#MDC.L	Mediclinic International plc
MDC_L_data = DataReader('MDC.L',  'yahoo', datetime(2015, 2, 20), datetime(2018, 2, 20))


# In[35]:


#Anglo American plc (AAL.L)
AAL_L_data = DataReader('AAL.L',  'yahoo', datetime(2015, 2, 20), datetime(2018, 2, 20))


# In[33]:


#Aggreko plc (AGK.L)
AGK_L_data = DataReader('AGK.L',  'yahoo', datetime(2015, 2, 20), datetime(2018, 2, 20))


# In[34]:


#Babcock International Group plc (BAB.L)
BAB_L_data = DataReader('BAB.L',  'yahoo', datetime(2015, 2, 20), datetime(2018, 2, 20))


# In[36]:


#Tesco PLC (TSCO.L)
TSCO_L_data = DataReader('TSCO.L',  'yahoo', datetime(2015, 2, 20), datetime(2018, 2, 20))


# In[66]:


plt.figure(figsize=(16,9))
plt.title("FTSE 100 and 30 components of it")
plt.plot(ftse_data['Close'],"k-",label="FTSE 100",lw=5.0)
plt.plot(VOD_L_data['Close'],label="VOD.L")
plt.plot(SHP_L_data['Close'],label="SHP.L")
plt.plot(BATS_L_data['Close'],label="BATS.L")
plt.plot(SDR_L_data['Close'],label="SDR.L")
plt.plot(RDSA_L_data['Close'],label="RDSA.L")
plt.plot(CPG_L_data['Close'],label="CPG.L")
plt.plot(CCH_L_data['Close'],label="CCH.L")
plt.plot(SMIN_L_data['Close'],label="SMIN.L")
plt.plot(SKY_L_data['Close'],label="SKY.L")
plt.plot(DLG_L_data['Close'],label="DLG.L")
plt.plot(SSE_L_data['Close'],label="SSE.L")
plt.plot(NMC_L_data['Close'],label="NMC.L")
plt.plot(PPB_L_data['Close'],label="PPB.L")
plt.plot(ANTO_L_data['Close'],label="ANTO.L")
plt.plot(PRU_L_data['Close'],label="PRU.L")
plt.plot(STJ_L_data['Close'],label="STJ.L")
plt.plot(GFS_L_data['Close'],label="GFS.L")
plt.plot(AHT_L_data['Close'],label="AHT.L")
plt.plot(CCL_L_data['Close'],label="CCL.L")
plt.plot(RTO_L_data['Close'],label="RTO.L")
plt.plot(CNA_L_data['Close'],label="CNA.L")
plt.plot(EXPN_L_data['Close'],label="EXPN.L")
plt.plot(EZJ_L_data['Close'],label="EZJ.L")
plt.plot(SMT_L_data['Close'],label="SMT.L")
plt.plot(TUI_L_data['Close'],label="TUI.L")
plt.plot(MDC_L_data['Close'],label="MDC.L")
plt.plot(AAL_L_data['Close'],label="AAL.L")
plt.plot(AGK_L_data['Close'],label="AGK.L")
plt.plot(BAB_L_data['Close'],label="BAB.L")
plt.plot(TSCO_L_data['Close'],label="TSCO.L")
plt.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.)
plt.ylabel('Stock price')
plt.grid()
plt.show()

