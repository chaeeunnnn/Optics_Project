import streamlit as st
import numpy as np
import plotly.graph_objs as go

def main():
    st.title('🌈 Refractive Index Data Explorer ')

    # Navigation
    st.sidebar.title('👇 See what we can do')
    pages = ['Home', 'Data Visualization', 'About']
    page = st.sidebar.radio('Select a Page:', pages)

    if page == 'Home':
        display_home_page()
    elif page == 'Data Visualization':
        display_interactive_explorer_page()
    elif page == 'About':
        display_about_page()

def display_home_page():
    st.header('Welcome to the Optics Class at Yonsei! 🔍')
    st.write('👉 This is a simple demo for the Optics class at Yonsei University, Fall 2023. This tool allows you to explore optical properties of various materials, including refractive index data, optical constants, and more. 😊')

    # Sellmeier equation
def sellmeier(wavelength, B, C):
    wl_squared = wavelength ** 2
    n_squared = 1 + (B[0] * wl_squared) / (wl_squared - C[0]) + (B[1] * wl_squared) / (wl_squared - C[1]) + (B[2] * wl_squared) / (wl_squared - C[2])
    return np.sqrt(n_squared)

def display_interactive_explorer_page():
    st.title("Interactive Refractive Index Explorer")

    # Humorous and educational explanation
    st.write("""
    ## 👀 Ever wondered why we see rainbows?
    It's all about light bending like it's in a yoga class 
             when it passes through different materials! 
             This tool lets you play with light's bending 
             powers (aka refractive index) based on what 
             it's traveling through. Pick a material and 
             watch how light bends at different wavelengths. 
             It's like choosing the path for light in its journey 
             through the universe! 🌟
    """)

    st.caption("📢 The values provided here are general representative values, and in actual applications or research, it may be necessary to find accurate measurements or values that fit specific conditions.")

    # Material selection
    materials = ["BK7 Glass", "Silica", "Water"]
    selected_materials = st.multiselect("👇 Select Material", materials, default=materials)

    # Slider for wavelength range
    wavelength = st.slider("👇 Select Wavelength Range (in micrometers)", 0.1, 5.0, (0.2, 4.0))

    # Coefficients for BK7 Glass and Silica
    coeffs = {
        "BK7 Glass": ([1.03961212, 0.231792344, 1.01046945], [6.00069867e-3, 2.00179144e-2, 103.560653]),
        "Silica": ([0.6961663, 0.4079426, 0.8974794], [4.67914826e-3, 1.35120631e-2, 97.9340025]),
        "Water": ([0.758, 0.097, 0.278], [0.005, 0.01, 120])
    }

    # Plotting
    wl_range = np.linspace(wavelength[0], wavelength[1], 500)
    fig = go.Figure()

    for material in selected_materials:
        n = sellmeier(wl_range, *coeffs[material])
        fig.add_trace(go.Scatter(x=wl_range, y=n, mode='lines', name=material,
                                 hoverinfo='x+y', hovertemplate='Wavelength: %{x:.3f} µm<br>n: %{y:.3f}'))

    fig.update_layout(title='Refractive Index vs. Wavelength',
                      xaxis_title='Wavelength (μm)',
                      yaxis_title='Refractive Index',
                      hovermode='closest',
                      plot_bgcolor='white',
                      xaxis=dict(showgrid=True),
                      yaxis=dict(showgrid=True))
    st.plotly_chart(fig, use_container_width=True)



def display_about_page():
    st.header('About')
    st.write('Thank you for visiting here today! 😊 Just a super simple demo tool powered by LLM(ChatGPT4) for a class project, might be implemented more if necessary. Hope it was helpful ✨ Any questions: chaeeunl2547@gmail.com')

if __name__ == '__main__':
    main()
