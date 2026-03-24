# Presentación de la imagen generada

La figura presenta la distribución masa–radio de exoplanetas con valores correctamente definidos, utilizando datos del *NASA Exoplanet Archive*.

La base de datos proporcionada para esta misión solo nos proporciona información sobre el nombre, el radio y la masa de cada uno de los planetas, y aunque no conocemos directamente la composición, sí podemos compararlos con modelos teóricos que predicen cómo debería escalar el radio con la masa para planetas compuestos por distintos materiales. Las curvas continuas que aparecen en la imagen son precisamente modelos de composición sacados del artículo de Seager et al. (2007), disponible en https://militzer.berkeley.edu/papers/34_seager_kuchner_hier-majumder_militzer_2007.pdf.

Este artículo presenta una relación que siguen los exoplanetas entre el radio de un planeta y su masa:

$$R(M) = r_1 \cdot 10^{\,k_1 + \frac{1}{3}\log_{10}\left(\frac{M}{m_1}\right) - k_2 \left(\frac{M}{m_1}\right)^{k_3}}$$

donde $M$ es la masa del planeta en masas terrestres, $R$ es el radio del planeta en unidades terrestres, $k_1 = -0.20945$ y $k_2 = 0.0804$ son constantes, y $m_1$ y $r_1$ son parametros para modelar la composición.

Cada curva del diagrama corresponde a una elección específica de $m_1$ y $r_1$, lo que permite modelar distintos tipos de planetas ideales. Para nuestra gráfica se utilizaron los siguientes parámetros:

Exoplaneta de hierro puro (100% Fe): $m_1 = 4.34$ y $r_1 = 2.23$

Planetas similares a la Tierra (67% MgSiO₃ + 33% Fe): $m_1 = 6.41$ y $r_1 = 2.84$

Planetas de silicatos puros (100% MgSiO₃): $m_1 = 7.38$ y $r_1 = 3.58$

Planetas de tres capas (Fe + MgSiO₃ + H₂O:$ m_1 = 6.41$ y $r_1 = 3.6$

Planetas de agua pura (100% H₂O): $m_1 = 8.16$ y $r_1 = 4.73$

Un planeta rocoso es aquel cuya atmosfera tiene un tamaño despreciable comparado con el resto del planeta, así que la curva de hierro puro es un limite que nos permite catalogar exoplanetas rocosos densos pues debajo de esta curva están todos los planetas que tienen una densidad mayor que la del hierro, que es uno de los metales más densos que se esperaría encontrar en el planeta, por lo que seguramente su atmosfera es despreciable.

Entre la curva de hierro puro y la curva de 67% MgSiO₃ + 33% Fe están los planetas que son más densos que nuestro planeta, pero menos densos que el hierro. Aquí estarían los demás candidatos razonables a ser planetas rocosos densos, sin embargo, no podemos estar seguro de ello pues podrían estar hechos de materiales densos y tener una atmosfera de un tamaño no despreciable, lo que los descatalogaría como planetas rocosos.

Todos los planetas que están por encima de la curva de 67% MgSiO₃ + 33% Fe, pero debajo de alguna de las curvas de 100% MgSiO₃ y de Fe + MgSiO₃ + H₂ son planetas que podrían ser rocosos, pero que su densidad sugiere que no lo son. Si fuesen planetas rocosos serían planetas compuestos principalmente por silicatos.

Los planetas de color azul son planetas que para que sean rocosos deben estar hechos principamente de agua o de materiales con una densidad similar. Lo esperado es que planetas con esta densidad sean gaseosos tal cómo ocurre con Jupiter que estaría pintado de este color.

La clasificación de los gigantes gaseosos esponjosos de la gráfica se hace combinando un criterio de masa y uno de densidad. El umbral de masa se toma del trabajo de Hatzes & Rauer (2015), disponible en https://sci-hub.hlgczx.com/10.1088/2041-8205/810/2/L25, quienes proponen definir planetas gigantes como aquellos con masas superiores a 0.3 masas jovianas, equivalente a aproximadamente 95.34 masas terrestres. A este criterio se le añade una condición de baja densidad media, fijada en 0.3 g/cm³, para que el gigante sea gaseoso esponjoso, pues su densidad media sugiere que el planeta está conformado por gases livianos.

Finalmente, los planetas que no cumplen ninguno de los criterios anteriores se agrupan en una categoría residual llamada en el gráfico "Otros planetas".


## Transición entre planetas rocosos y gigantes gaseosos esponjosos

Cómo la masa y el radio del planeta no son suficientes para clasificar con exactitud si un planeta es rocoso denso o gigante gaseoso esponjoso, solo podemos trazar una pequeña frontera dónde es posible encontrar planetas rocosos hechos de agua y gigantes con una densidad pequeña. Esta frontera corresponde a la pequeña región en dónde la curva azul se acerca al limite para ser considerado un planeta gaseoso gigante, y corresponde a planetas con masas cercanas a las 100 masas terrestres y con un radio de aproximadamente 4 radios terrestres.
