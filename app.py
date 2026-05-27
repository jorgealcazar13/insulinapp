import streamlit as st

# Configuración de la página móvil
st.set_page_config(page_title="InsulinApp - MF", page_icon="💉", layout="centered")

st.title("💉 InsulinApp - Medicina Familiar")
st.write("Guía rápida de inicio y ajuste de insulina (Artículos 2016 - 2026)")
st.markdown("---")

# Menú de navegación por pestañas (Tabs)
tab1, tab2, tab3, tab4 = st.tabs(["📌 Inicio DM2", "📊 Titulación", "🧪 Nuevas Insulinas", "⚠️ Seguridad"])

with tab1:
    st.header("Criterios de Inicio Ambulatorio")
    st.info("**¿Cuándo iniciar?** Mantener fármacos orales (Metformina) y agregar basal si:")
    
    st.markdown("""
    * **HbA1c ≥ 7.5%:** Considerar inicio de insulina basal combinada.
    * **HbA1c > 9.0% o Catabolismo:** Inicio **esencial y obligatorio** (pérdida de peso, poliuria, polidipsia).
    """)
    
    st.subheader("Cálculo de Dosis Inicial")
    metodo = st.radio("Selecciona método de cálculo:", ["Por Peso (U/kg)", "Dosis Fija"])
    
    if metodo == "Por Peso (U/kg)":
        peso = st.number_input("Peso del paciente (kg):", min_value=30, max_value=150, value=70)
        factor = st.slider("Factor (U/kg/día):", 0.1, 0.2, 0.1, step=0.05)
        dosis = round(peso * factor)
        st.success(f"Dosis inicial calculada: **{dosis} unidades** por la noche.")
    else:
        st.success("Dosis inicial sugerida: **10 unidades** al día por la noche.")

with tab2:
    st.header("Algoritmo de Titulación en Casa")
    st.write("Meta estándar de glucosa capilar en ayuno: **80 - 130 mg/dL**")
    
    glucosa = st.number_input("Introduce el promedio de glucosa en ayunas (3 días):", min_value=40, max_value=400, value=140)
    
    if glucosa < 70:
        st.error("🚨 **HIPOGLUCEMIA:** Reducir la dosis de 2 a 4 unidades (o bajar 10% - 20%).")
    elif 80 <= glucosa <= 130:
        st.success("✅ **EN META:** Mantener la dosis actual sin cambios.")
    elif glucosa > 130:
        st.warning("⚠️ **FUERA DE META:** Aumentar **+2 unidades** a la dosis basal.")

with tab3:
    st.header("Fichas de Nuevas Insulinas (Actualización 2026)")
    
    with st.expander("Glargina U-300 (Toujeo) - Ultraprolongada"):
        st.write("* **Mecanismo:** 3 veces más concentrada (menos volumen de inyección).")
        st.write("* **Perfil:** Liberación lineal sin pico, duración de 24-36 horas.")
        st.write("* **Ventaja:** Reduce significativamente el riesgo de hipoglucemia nocturna.")
        
    with st.expander("Degludec (Tresiba) - Ultraprolongada"):
        st.write("* **Mecanismo:** Formación de multihexámeros subcutáneos, duración > 42 horas.")
        st.write("* **Ventaja:** Perfil plano y **flexibilidad horaria** en la aplicación diaria.")
        
    with st.expander("Fiasp / Lyumjev - Ultrarrápidas"):
        st.write("* **Mecanismo:** Inicio de acción en 1-2.5 min gracias a aditivos vasculares.")
        st.write("* **Uso Clínico:** Aplicación 0-20 min después de comer. Ideal para apetito variable.")
        
    with st.expander("Icodec - Semanal (Futuro del apego)"):
        st.write("* **Perfil:** Duración > 168 horas, vida media de 1 semana.")
        st.write("* **Impacto:** **1 inyección semanal** en lugar de 365 inyecciones anuales.")

with tab4:
    st.header("Alertas de Seguridad Críticas")
    st.markdown("""
    * ❌ **Uso de la sigla 'u':** **PROHIBIDO.** La 'u' manuscrita se confunde con un cero en las recetas, causando sobredosis de hasta 10 veces (ej. '10u' puede leerse como '100'). Escribe siempre la palabra completa **'unidades'**.
    * ❌ **Mezcla de Análogos:** Las insulinas de acción prolongada o ultraprolongada (Glargina, Degludec, Detemir) **nunca** deben mezclarse en la misma jeringa con otras moléculas por alteración drástica de su pH.
    """)
