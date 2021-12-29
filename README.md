# GR
Bunch of codes for general relativity: e.g. calculation of: curvatures, trajectories, etc.

In files "Metrica di Schawrzchild.ipynb" and "Tensore_di_Rieman.nb" the Riemann tensor, the Ricci tensor and the scalar curvature of Ricci are calculated, starting from metric:

<img src="https://latex.codecogs.com/svg.image?\\R^{\mu}_{\nu&space;\rho&space;\sigma}&space;=&space;\partial_{\rho}\Gamma^{\mu}_{\nu\sigma}-&space;\partial_{\sigma&space;}\Gamma^{\mu}_{\nu\rho}&space;&plus;&space;&space;\Gamma^{\mu}_{\rho&space;\lambda}&space;\Gamma^{\lambda}_{\nu&space;\sigma}&space;&space;-&space;\Gamma^{\mu}_{\sigma\lambda}&space;\Gamma^{\lambda}_{\nu&space;\rho}\\\\R_{\nu&space;\sigma}=&space;R^{\mu}_{\nu&space;\mu&space;\sigma}\\\\R&space;=&space;g^{\nu&space;\sigma}&space;R_{\nu&space;\sigma}" title="\\R^{\mu}_{\nu \rho \sigma} = \partial_{\rho}\Gamma^{\mu}_{\nu\sigma}- \partial_{\sigma }\Gamma^{\mu}_{\nu\rho} + \Gamma^{\mu}_{\rho \lambda} \Gamma^{\lambda}_{\nu \sigma} - \Gamma^{\mu}_{\sigma\lambda} \Gamma^{\lambda}_{\nu \rho}\\\\R_{\nu \sigma}= R^{\mu}_{\nu \mu \sigma}\\\\R = g^{\nu \sigma} R_{\nu \sigma}" />

where the Christoffel symbols are given by:

<img src="https://latex.codecogs.com/svg.image?\Gamma^{\mu}_{\nu&space;\rho}&space;=&space;\frac{1}{2}&space;g^{\mu&space;\lambda}(\partial_{\nu}&space;g_{\lambda&space;\rho}&space;&plus;&space;\partial_{\rho}&space;g_{\lambda&space;\nu}&space;-&space;\partial_{\lambda}&space;g_{\nu&space;\rho})" title="\Gamma^{\mu}_{\nu \rho} = \frac{1}{2} g^{\mu \lambda}(\partial_{\nu} g_{\lambda \rho} + \partial_{\rho} g_{\lambda \nu} - \partial_{\lambda} g_{\nu \rho})" />

In "geodetica sfera.nb" the geodesic on a sphere, which we know to be the circle of maximum radius, is calculated by solving the equation of motion:

<img src="https://latex.codecogs.com/svg.image?\frac{d^2x^{\mu}}{d\lambda^2}&space;-&space;\Gamma^{\mu}_{\nu&space;\rho}&space;\frac{dx^{\nu}}{d\lambda}&space;\frac{dx^{\rho}}{d\lambda}&space;=&space;0" title="\frac{d^2x^{\mu}}{d\lambda^2} - \Gamma^{\mu}_{\nu \rho} \frac{dx^{\nu}}{d\lambda} \frac{dx^{\rho}}{d\lambda} = 0" />

In "E-F_coor.py" the radial trajectories of light are considered in coordinates that solve the apparent singularity in rs = 2M. From the Schawrzchild metric it is obtained:

<img src="https://latex.codecogs.com/svg.image?\\ds^2&space;=&space;0&space;\Rightarrow&space;\frac{dr}{dx^0}&space;=&space;&space;\pm&space;\frac{r-r_s}{r}&space;\\r&space;&plus;&space;r_s&space;\ln(r-r_s)&space;=&space;\pm&space;x^0&space;&plus;&space;cost&space;" title="\\ds^2 = 0 \Rightarrow \frac{dr}{dx^0} = \pm \frac{r-r_s}{r} \\r + r_s \ln(r-r_s) = \pm x^0 + cost " />

where the + sign identifies the outgoing trajectories and the - the incoming ones

we can define:

<img src="https://latex.codecogs.com/svg.image?\\\begin{cases}v&space;=&space;x^0&space;&plus;&space;r&space;&plus;&space;r_s&space;\ln(r-r_s)&space;\\&space;r&space;=&space;r&space;\\\end{cases}&space;\\\\\text{and&space;in&space;this&space;coordinates:}\\\\ds^2&space;=&space;\Bigl(1&space;-&space;\frac{r_s}{r}\Bigr)dv^2&space;-&space;2dvdr&space;\\&space;\\\text{therefore&space;there&space;are&space;only&space;outgoing&space;trajectories.&space;in&space;the&space;code&space;the&space;coordinates&space;are&space;used:}\\\begin{cases}\overline{x^0}&space;=&space;v&space;-&space;r&space;\\&space;r&space;=&space;r&space;\\\end{cases}&space;" title="\\\begin{cases}v = x^0 + r + r_s \ln(r-r_s) \\ r = r \\\end{cases} \\\\\text{and in this coordinates:}\\\\ds^2 = \Bigl(1 - \frac{r_s}{r}\Bigr)dv^2 - 2dvdr \\ \\\text{therefore there are only outgoing trajectories. in the code the coordinates are used:}\\\begin{cases}\overline{x^0} = v - r \\ r = r \\\end{cases} " />


