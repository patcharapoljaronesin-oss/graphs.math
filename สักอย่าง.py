import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, sympify, lambdify

import streamlit as st
import streamlit.components.v1 as components
import base64

#st.audio('[Hatsune Miku (Text To Speech)]Here!......raphs.mp3', autoplay=True)

st.title("Miku.Math")

def play():
    st.session_state.play = True

xIn = st.text_input('ใส่ค่า $x$') 
xlist = list(map(float, xIn.split()))
X = symbols('x')
eq = st.text_input('ใส่สมการของ $y$')
if xIn != "" and eq != "":
    exper = sympify(eq)
    f = lambdify(X, exper, "numpy")
    xmax = max(xlist)
    xmin = min(xlist)
    #print(xmax,xmin)
    x = np.linspace(float(xmin),float(xmax),1000)
    y = f(x)


    def setup(xmin,xmax,ymin,ymax,tr):
        fig,ax = plt.subplots(figsize=(8,6) , dpi=200)
        fig.set_facecolor('#ffffff')
        fig.tight_layout()
        ax.set_xlim(xmin-1,xmax+1)
        ax.set_ylim(ymin-1,ymax+1)
        ax.spines['left'].set_position('zero')
        ax.spines['bottom'].set_position('zero')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        ax.set_xlabel(r'$x$', size=14,labelpad=24,x=1.02)
        ax.set_ylabel(r'$y$', size=14,labelpad=21,y=1.02, rotation=0)
        ax.xaxis.set_label_coords(1.03,0.505)
        ax.yaxis.set_label_coords(0.50,1.03)

        plt.text(0.5,0.5, r'$0$', ha='right',va='top',transform=ax.transAxes,horizontalalignment='center')

        xtick = np.arange(xmin,xmax+1, tr)
        ytick = np.arange(ymin,ymax+1, tr)
    

        ax.grid(True)

        ans = ""

        for i in range(0,len(xlist)):
            #print(i)
            if float(xlist[i]) < 0.0:
                 xtext = float(xlist[i]) - (xmax * (50/100))
                 ytext = f(float(xlist[i])) - 1
                 print(xtext)
            elif float(xlist[i]) == 0:
                 xtext = 0
                 ytext = f(float(xlist[i])) - (ymax * (20/100))
                 print(xtext)
            elif float(xlist[i]) > 0.0:
                 xtext = float(xlist[i]) + (xmax * (30/100))
                 ytext = f(float(xlist[i])) - 2
                 print(xtext)
            ax.annotate(f"({xlist[i]},{f(float(xlist[i]))})", xy=(float(xlist[i]),f(float(xlist[i]))), 
                    xytext=(xtext, ytext), 
                    arrowprops=dict(facecolor='black',))
            ans += f" {f(float(xlist[i]))} ,"
        
        ax.plot(x,y)
        st.markdown(f'$y$ = {ans}')
        return fig

    fig = setup(xmax*-1,xmax,f(xmax*(101/100))*-1,f(xmax*(101/100)),1)

    if eq != '' or xIn != '':
        with open("[Hatsune Miku (Text To Speech)]Here!......raphs.mp3", "rb") as f:
            audio = base64.b64encode(f.read()).decode()

        components.html(f"""
        <audio id="player">
            <source src="data:audio/mp3;base64,{audio}" type="audio/mp3">
        </audio>

        <script>
        document.getElementById("player").play();
        </script>
        """, height=0)
        st.text("ตัวอย่าง:")
        st.pyplot(fig)
        plt.close()
