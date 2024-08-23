{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "df09350a-a17b-4d9d-ab60-de58d70a7010",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "\n",
    "# Title\n",
    "st.title('Environmental Data Dashboard')\n",
    "\n",
    "# Upload CSV files\n",
    "uploaded_file = st.file_uploader(\"Choose a CSV file\", type=\"csv\")\n",
    "if uploaded_file is not None:\n",
    "    data = pd.read_csv(uploaded_file)\n",
    "    st.write(data.head())\n",
    "\n",
    "    # Correlation Matrix\n",
    "    st.subheader('Correlation Matrix')\n",
    "    corr_matrix = data.corr()\n",
    "    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')\n",
    "    st.pyplot(plt)\n",
    "\n",
    "    # Display histograms\n",
    "    st.subheader('Histograms')\n",
    "    numeric_columns = data.select_dtypes(['float64', 'int64']).columns\n",
    "    for col in numeric_columns:\n",
    "        st.write(f'Histogram for {col}')\n",
    "        fig, ax = plt.subplots()\n",
    "        data[col].hist(bins=20, ax=ax)\n",
    "        st.pyplot(fig)\n",
    "\n",
    "    # Additional analysis or visualization\n",
    "    st.subheader('Additional Analysis')\n",
    "    # Add more analysis here if needed\n",
    "\n",
    "else:\n",
    "    st.write(\"Please upload a CSV file to start analysis.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "1c97a098-af86-496e-bf94-b2a1fbc205b5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "2a8d35e9-6d83-4090-aa9d-1d74540dfea9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
