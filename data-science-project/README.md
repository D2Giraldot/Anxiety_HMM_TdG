# Trabajo de grado: Modelación probabilística y dinámica de la ansiedad mediante técnicas de clustering y Modelos Ocultos de Márkov

## Abstract.
Este estudio propone un marco probabilístico para caracterizar el comportamiento dinámico de la ansiedad a partir de variables psicológicas y conductuales. La aproximación integra técnicas de aprendizaje no supervisado, mode-los de probabilidad no normales y Modelos Ocultos de Márkov (HMM) con el fin de identificar perfiles observables, inferir estados latentes y describir su evolución temporal. Indicadores como el nivel de estrés percibido, el sueño, la actividad física y el consumo de estimulantes se utilizan para construir agrupaciones conductuales que alimentan el mo-delo estocástico. Paralelamente, se evalúa la estructura estadística del indicador transformado de ansiedad mediante distribuciones continuas, con el propósito de obtener una representación parsimoniosa de su comportamiento marginal. Los resultados muestran que la ansiedad presenta una dinámica marcada por la persistencia en estados de riesgo mode-rado o alto, así como una distribución asimétrica que concentra sus episodios más críticos en niveles bajos del indicador de bienestar. El marco resultante ofrece una base técnica para modelar la ansiedad como un proceso dinámico y estocás-tico, y constituye un insumo potencial para sistemas de monitoreo emocional y para la toma de decisiones en salud men-tal ocupacional 


## Descripción
Análisis y modelado de variables relacionadas con niveles de ansiedad y hábitos. El flujo incluye exploración, selección de variables, clustering y modelado HMM, seguido de evaluación y estabilización de distribuciones.

## Estructura
- `notebooks/Final/01_EDA.ipynb`: exploración y limpieza; selección de variables observables.
- `notebooks/Final/02_ModelacionHMM.ipynb`: clustering (KMeans/DBSCAN/KMedoids), reducción de dimensionalidad y construcción de matrices de transición/emisión.
- `notebooks/Final/03_Estabilización_Evaluación.ipynb`: evaluación de distribuciones, validación (F1, KS, Wasserstein) y análisis de estacionariedad.
- `notebooks/datalab/`: cuadernos de prueba.
- `data/raw/`: datos originales.
- `data/stage/`: datos intermedios/limpios.
- `data/analytics/`: salidas y evidencias (CSV, HTML, PNG) de los notebooks finales.
- `src/utils.py`: utilidades para partición de datos.
- `requirements.txt`: dependencias del proyecto.

## Requerimientos
pandas
numpy
matplotlib
seaborn
scipy
scikit-learn
scikit-learn-extra
pyclustering
plotly
statsmodels


## Abrir los notebooks de notebooks/Final y ejecutar secuencialmente (01 → 02 → 03). 

### Evidencias y resultados
* CSV generados: data/analytics/df_final_modelacion.csv, df_var_obs_kmeans.csv, df_var_no_obs_kmeans.csv, df_evolucion_distribucion.csv.
* Visualizaciones y reportes: clusters_kmeans_3_var_obs_final.html, cluster_kmeans3_var_no_obs.html, y gráficos PNG (matrices de transición/emisión, distribuciones estacionarias, evaluación VaR).
* Los gráficos y HTML corresponden a las ejecuciones de los notebooks finales.

### Uso
* Empezar con 01_EDA.ipynb para limpiar/entender los datos.
* Correr 02_ModelacionHMM.ipynb para clustering, PCA y cálculo de matrices HMM.
* Finalizar con 03_Estabilización_Evaluación.ipynb para validar distribuciones y métricas de desempeño.

### Notas
* Los notebooks en notebooks/datalab son exploratorios y no forman parte del flujo principal.
Ajusta rutas si mueves el proyecto; las salidas se guardan en data/analytics.


