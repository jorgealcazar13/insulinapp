import streamlit as st

# Configuración de la página móvil
st.set_page_config(page_title="InsulinApp - MF", page_icon="💉", layout="centered")

st.title("💉 InsulinApp - Medicina Familiar")
st.write("Guía práctica de inicio, dosificación y tiempos de aplicación")
st.markdown("---")

# Menú de navegación por pestañas optimizado para tu consulta diaria
tab1, tab2, tab3, tab4 = st.tabs(["📌 Inicio DM2", "📊 Titulación", "⏱️ Tiempos y Aplicación", "⚠️ Seguridad"])

with tab1:
    st.header("Criterios de Inicio Ambulatorio")
    st.info("**¿Cuándo iniciar?** Mantener fármacos orales (Metformina) y agregar basal si:")
    
    st.markdown("""
    * **HbA1c ≥ 7.5%:** Considerar inicio de insulina basal combinada con los orales[cite: 22].
    * **HbA1c > 9.0% o Catabolismo:** Inicio **esencial y obligatorio**[cite: 22]. Evaluar síntomas clínicos como pérdida de peso acelerada, poliuria o polidipsia[cite: 156].
    """)
    
    st.subheader("Cálculo de Dosis Inicial")
    metodo = st.radio("Selecciona método de cálculo:", ["Por Peso (U/kg)", "Dosis Fija"])
    
    if metodo == "Por Peso (U/kg)":
        peso = st.number_input("Peso del paciente (kg):", min_value=30, max_value=150, value=70)
        factor = st.slider("Factor inicial (U/kg/día):", 0.1, 0.2, 0.1, step=0.05)
        dosis = round(peso * factor)
        st.success(f"Dosis inicial calculada: **{dosis} unidades** al día por la noche[cite: 430].")
    else:
        st.success("Dosis inicial sugerida: **10 unidades** al día por la noche.")

with tab2:
    st.header("Algoritmo de Titulación en Casa")
    st.write("Meta estándar de glucosa capilar en ayuno: **80 - 130 mg/dL**")
    
    glucosa = st.number_input("Introduce el promedio de glucosa en ayunas (3 días):", min_value=40, max_value=400, value=140)
    
    if glucosa < 70:
        st.error("🚨 **HIPOGLUCEMIA:** Reducir la dosis de 2 a 4 unidades de inmediato (o bajar 10% - 20% de la dosis)[cite: 156, 441].")
    elif 80 <= glucosa <= 130:
        st.success("✅ **EN META:** Mantener la dosis actual sin cambios.")
    elif glucosa > 130:
        st.warning("⚠️ **FUERA DE META:** Aumentar **+2 unidades** a la dosis basal actual (evaluar promedio de 3 días).")

with tab3:
    st.header("Tiempos de Acción y Administración")
    st.write("Usa esta guía para orientar al paciente sobre el momento exacto de su inyección en relación con los alimentos:")
    
    with st.expander("Insulina de Acción Intermedia (NPH / Humulin N / Novolin N)"):
        st.markdown("""
        * **Inicio de acción:** 1 a 4 horas[cite: 83].
        * **Pico máximo:** 4 a 10 horas [cite: 423] (¡Ojo! Monitorear riesgo de hipoglucemia en el pico [cite: 156]).
        * **Duración:** 10 a 18 horas[cite: 423].
        * **Momento de aplicación:** Generalmente por la noche (antes de dormir)[cite: 118]. Si se requieren dosis altas, se divide en dos aplicaciones al día (2/3 por la mañana y 1/3 por la noche)[cite: 62].
        """)
        
    with st.expander("Insulina de Acción Prolongada (Glargina / Lantus / Basaglar)"):
        st.markdown("""
        * **Inicio de acción:** 1 a 4 horas[cite: 83].
        * **Pico máximo:** **Sin pico** (liberación continua y estable)[cite: 83, 337].
        * **Duración:** 20 a 24 horas[cite: 340].
        * **Momento de aplicación:** Una vez al día, estrictamente a la misma hora todos los días (independientemente de las comidas)[cite: 58, 59].
        """)
        
    with st.expander("Insulina de Acción Corta (Regular / Humulin R / Novolin R)"):
        st.markdown("""
        * **Inicio de acción:** 30 a 60 minutos[cite: 83].
        * **Pico máximo:** 2 a 5 horas[cite: 83].
        * **Duración:** 4 a 12 horas[cite: 83].
        * **Momento de aplicación:** **30 a 45 minutos antes de la comida**[cite: 73]. Requiere una disciplina estricta en los horarios para evitar desfases con el pico de carbohidratos[cite: 74].
        """)

    with st.expander("Análogos de Acción Rápida (Lispro / Humalog / Aspart / NovoLog)"):
        st.markdown("""
        * **Inicio de acción:** 5 a 15 minutos[cite: 423].
        * **Pico máximo:** 30 a 90 minutos[cite: 423].
        * **Duración:** 3 a 6 horas[cite: 83].
        * **Momento de aplicación:** **15 minutos antes de empezar a comer** o justo al iniciar el alimento debido a su rápido inicio[cite: 69, 423].
        """)

with tab4:
    st.header("Alertas de Seguridad Críticas")
    st.markdown("""
    * ❌ **Uso de la sigla 'u':** **STRICTAMENTE PROHIBIDO.** La 'u' manuscrita se confunde fácilmente con un cero en los expedientes o recetas, provocando errores de sobredosificación de hasta 10 veces (ej. '10u' puede leerse y administrarse como '100 unidades')[cite: 119, 120]. Siempre escribe o teclea la palabra completa **'unidades'**[cite: 121].
    * ❌ **Mezcla física de jeringas:** La insulina Regular y la NPH se pueden mezclar de forma segura en la misma jeringa (aspirando siempre primero la Regular que es clara, y luego la NPH que es turbia)[cite: 148, 149]. **Sin embargo, los análogos de acción prolongada (Glargina, Degludec, Detemir) NUNCA deben mezclarse** con ninguna otra insulina en la misma jeringa debido a diferencias críticas en su pH[cite: 146, 147].
    """)
