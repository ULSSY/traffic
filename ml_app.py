import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

def run_ml_app() :
    st.subheader('Machine Learning ����')

    df = pd.read_csv('data/���α���.csv', encoding='CP949')
    df = df.loc[:,'�߻��Ǽ�':'�λ�Ű�']
    # 1. ��������, �����͸� �Է¹޽��ϴ�.
    gender = st.radio('�õ��� �Է��ϼ���.', ['��õ', '���','����','����','����','���','�泲','����','����','����','����','�뱸','�λ�','���','���','�泲'])
    if gender == '��õ' :
        st.selectbox('�ñ����� �Է��ϼ���.', ['�߱�', '����','����','����','������','����','������','��籸'])
        
        st.subheader('�� �÷��� ������׷� Ȯ��')

        selected_column=st.selectbox('�÷��� �����ϼ���',df.columns)

        bins=st.slider('bin�� ���� ����',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('�� �÷��� ���ġ')
        st.dataframe(df.describe())

    elif gender == '���' :
        st.selectbox('�ñ����� �Է��ϼ���.', ['������', '������','�����ν�','�Ⱦ��','��õ��','�Ȼ��','���ý�','�����','������','���ֽ�','���ֽ�','ȭ����','�����','����','���ֽ�','��õ��','����','����','��õ��','���ν�','�ȼ���','������','������','�����ֽ�','�����','�ǿս�','�ϳ���'])
        st.subheader('�� �÷��� ������׷� Ȯ��')

        selected_column=st.selectbox('�÷��� �����ϼ���',df.columns)

        bins=st.slider('bin�� ���� ����',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('�� �÷��� ���ġ')
        st.dataframe(df.describe())
    elif gender == '����' :
        st.selectbox('�ñ����� �Է��ϼ���.', ['��õ��', '���ֽ�','���ؽ�','������','���ʽ�','ȫõ��','Ⱦ����','��â��','������','��籺'])
        st.subheader('�� �÷��� ������׷� Ȯ��')

        selected_column=st.selectbox('�÷��� �����ϼ���',df.columns)

        bins=st.slider('bin�� ���� ����',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('�� �÷��� ���ġ')
        st.dataframe(df.describe())
    elif gender == '����' :
        st.selectbox('�ñ����� �Է��ϼ���.', ['���ϱ�', '������','������','������','���ı�','���ʱ�','��õ��','�߶���','�����','��õ��'])
        st.subheader('�� �÷��� ������׷� Ȯ��')

        selected_column=st.selectbox('�÷��� �����ϼ���',df.columns)

        bins=st.slider('bin�� ���� ����',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('�� �÷��� ���ġ')
        st.dataframe(df.describe())
    elif gender == '����' :
        st.selectbox('�ñ����� �Է��ϼ���.', ['����'])
        st.subheader('�� �÷��� ������׷� Ȯ��')

        selected_column=st.selectbox('�÷��� �����ϼ���',df.columns)

        bins=st.slider('bin�� ���� ����',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('�� �÷��� ���ġ')
        st.dataframe(df.describe())
    elif gender == '���' :
        st.selectbox('�ñ����� �Է��ϼ���.', ['û�ֽ�', '���ֽ�','��õ��','������','��õ��','������','��õ��','���걺','������','�ܾ籺','����'])
        st.subheader('�� �÷��� ������׷� Ȯ��')

        selected_column=st.selectbox('�÷��� �����ϼ���',df.columns)

        bins=st.slider('bin�� ���� ����',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('�� �÷��� ���ġ')
        st.dataframe(df.describe())
    elif gender == '�泲' :
        st.selectbox('�ñ����� �Է��ϼ���.', ['õ�Ƚ�', '���ɽ�','���ֽ�','�����','�ݻ걺','����','�ο���','��õ��','û�籺','ȫ����','���걺','������','����'])
        st.subheader('�� �÷��� ������׷� Ȯ��')

        selected_column=st.selectbox('�÷��� �����ϼ���',df.columns)

        bins=st.slider('bin�� ���� ����',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('�� �÷��� ���ġ')
        st.dataframe(df.describe())
    elif gender == '����' :
        st.selectbox('�ñ����� �Է��ϼ���.', ['�ϱ�', '���걸'])
        st.subheader('�� �÷��� ������׷� Ȯ��')

        selected_column=st.selectbox('�÷��� �����ϼ���',df.columns)

        bins=st.slider('bin�� ���� ����',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('�� �÷��� ���ġ')
        st.dataframe(df.describe())
    elif gender == '����' :
        st.selectbox('�ñ����� �Է��ϼ���.', ['����', '�߱�','����','������','�����'])
        st.subheader('�� �÷��� ������׷� Ȯ��')

        selected_column=st.selectbox('�÷��� �����ϼ���',df.columns)

        bins=st.slider('bin�� ���� ����',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('�� �÷��� ���ġ')
        st.dataframe(df.describe())
    elif gender == '����' :
        st.selectbox('�ñ����� �Է��ϼ���.', ['���ֽ�', '�����','������','������','������','���ֱ�','���ֱ�','�����','�ӽǱ�','��â��','��â��','�ξȱ�','�ͻ��'])
        st.subheader('�� �÷��� ������׷� Ȯ��')

        selected_column=st.selectbox('�÷��� �����ϼ���',df.columns)

        bins=st.slider('bin�� ���� ����',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('�� �÷��� ���ġ')
        st.dataframe(df.describe())
    elif gender == '����' :
        st.selectbox('�ñ����� �Է��ϼ���.', ['������', '��õ��','���ֽ�','�����','��籺','���','���ʱ�','������','���ﱺ','������','���ȱ�','����','������','�强��'])
        st.subheader('�� �÷��� ������׷� Ȯ��')

        selected_column=st.selectbox('�÷��� �����ϼ���',df.columns)

        bins=st.slider('bin�� ���� ����',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('�� �÷��� ���ġ')
        st.dataframe(df.describe())
    elif gender == '�뱸' :
        st.selectbox('�ñ����� �Է��ϼ���.', ['����', '����','�ϱ�','������','�޼���','�޼���'])
        st.subheader('�� �÷��� ������׷� Ȯ��')

        selected_column=st.selectbox('�÷��� �����ϼ���',df.columns)

        bins=st.slider('bin�� ���� ����',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('�� �÷��� ���ġ')
        st.dataframe(df.describe())
    elif gender == '�λ�' :
        st.selectbox('�ñ����� �Է��ϼ���.', ['�ϱ�', '�ؿ�뱸','������','������','���','���屺'])
        st.subheader('�� �÷��� ������׷� Ȯ��')

        selected_column=st.selectbox('�÷��� �����ϼ���',df.columns)

        bins=st.slider('bin�� ���� ����',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('�� �÷��� ���ġ')
        st.dataframe(df.describe())
    elif gender == '���' :
        st.selectbox('�ñ����� �Է��ϼ���.', ['���ֱ�'])
        st.subheader('�� �÷��� ������׷� Ȯ��')

        selected_column=st.selectbox('�÷��� �����ϼ���',df.columns)

        bins=st.slider('bin�� ���� ����',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('�� �÷��� ���ġ')
        st.dataframe(df.describe())
    elif gender == '���' :
        st.selectbox('�ñ����� �Է��ϼ���.', ['������', '��õ��','���ֽ�','�����','��籺','���','���ʱ�','������','���ﱺ','������','���ȱ�','����','������','�强��'])
        st.subheader('�� �÷��� ������׷� Ȯ��')

        selected_column=st.selectbox('�÷��� �����ϼ���',df.columns)

        bins=st.slider('bin�� ���� ����',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('�� �÷��� ���ġ')
        st.dataframe(df.describe())
    elif gender == '�泲' :
        st.selectbox('�ñ����� �Է��ϼ���.', ['������', '��õ��','���ֽ�','�����','��籺','���','���ʱ�','������','���ﱺ','������','���ȱ�','����','������','�强��'])
        st.subheader('�� �÷��� ������׷� Ȯ��')

        selected_column=st.selectbox('�÷��� �����ϼ���',df.columns)

        bins=st.slider('bin�� ���� ����',min_value=10,max_value=50)

        fig1=plt.figure()
        df[selected_column].hist(bins=bins)
        st.pyplot(fig1)

        st.subheader('�� �÷��� ���ġ')
        st.dataframe(df.describe())
    # # 2. �𵨿� �����Ѵ�.

    # # 2-1. �űԵ����͸� �����̷� �����.
    # new_data = np.array([gender_number, age, salary, debt, worth])
    # new_data = new_data.reshape(1, 5)

    # # 2-2. �����Ϸ��� �ΰ������� ������ �ҷ��´�.
    # scaler_X = joblib.load('data/scaler_X.pkl')
    # scaler_y = joblib.load('data/scaler_y.pkl')
    # regressor = joblib.load('data/regressor.pkl')

    # # 2-3. �űԵ����͸� ���Ľ����ϸ� �Ѵ�.
    # new_data = scaler_X.transform(new_data)

    # # 2-4. �ΰ����ɿ��� ������ �ϰ� �Ѵ�.
    # y_pred = regressor.predict(new_data)
    
    # # 2-5. ������ �����, �ٽ� ������� ������ ��� �Ѵ�. 
    # print(y_pred)

    # y_pred = scaler_y.inverse_transform(y_pred.reshape(1,1))
    # print(y_pred)

    # # 3. ���� ����� �� ��ú��忡 ǥ���Ѵ�.

    # btn = st.button('���� ��� ����')
    # # ����� �Ҽ������� �����µ�, �Ҽ��� �� ���ڸ������� ��������
    # # �ڵ� �����ϼ���.
    # if btn :
    #     st.write('���� ���! {:.1f} �޷��� ���� �� �� �ֽ��ϴ�.'.format(y_pred[0,0]))
    #     st.write('���� ���! {} �޷��� ���� �� �� �ֽ��ϴ�.'.format( round(y_pred[0,0], 1) ))