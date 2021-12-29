# GR
Bunch of codes for general relativity: e.g. calculation of: curvatures, trajectories, etc.

In files "Metrica di Schawrzchild.ipynb" and "Tensore_di_Rieman.nb" the Riemann tensor, the Ricci tensor and the scalar curvature of Ricci are calculated, starting from metric:

<img src="https://latex.codecogs.com/svg.image?\\R^{\mu}_{\hspace{2&space;mm}&space;\nu&space;\rho&space;\sigma}&space;=&space;\partial_{\rho}\Gamma^{\hspace{2&space;mm}&space;\mu}_{\nu&space;\hspace{2&space;mm}&space;\sigma}&space;-&space;\partial_{\sigma}&space;\Gamma^{\hspace{2&space;mm}&space;\mu}_{\nu&space;\hspace{2&space;mm}&space;\rho}&space;&plus;&space;\Gamma^{\hspace{2&space;mm}&space;\mu}_{\rho&space;\hspace{2&space;mm}&space;\lambda}&space;\Gamma^{\hspace{2&space;mm}&space;\lambda}_{\nu&space;\hspace{2&space;mm}&space;\sigma}&space;-&space;\Gamma^{\hspace{2&space;mm}&space;\mu}_{\sigma&space;\hspace{2&space;mm}&space;\lambda}&space;\Gamma^{\hspace{2&space;mm}&space;\lambda}_{\nu&space;\hspace{2&space;mm}&space;\rho}\\\\R_{\nu&space;\sigma}&space;&space;=&space;R^{\mu}_{\hspace{2&space;mm}&space;\nu&space;\mu&space;\sigma}&space;\\&space;&space;\\R&space;=&space;g^{\nu&space;\sigma}&space;R_{\nu&space;\sigma}&space;" title="\\R^{\mu}_{\hspace{2 mm} \nu \rho \sigma} = \partial_{\rho}\Gamma^{\hspace{2 mm} \mu}_{\nu \hspace{2 mm} \sigma} - \partial_{\sigma} \Gamma^{\hspace{2 mm} \mu}_{\nu \hspace{2 mm} \rho} + \Gamma^{\hspace{2 mm} \mu}_{\rho \hspace{2 mm} \lambda} \Gamma^{\hspace{2 mm} \lambda}_{\nu \hspace{2 mm} \sigma} - \Gamma^{\hspace{2 mm} \mu}_{\sigma \hspace{2 mm} \lambda} \Gamma^{\hspace{2 mm} \lambda}_{\nu \hspace{2 mm} \rho}\\\\R_{\nu \sigma} = R^{\mu}_{\hspace{2 mm} \nu \mu \sigma} \\ \\R = g^{\nu \sigma} R_{\nu \sigma} " />

where the Christoffel symbols are given by:

<img src="https://latex.codecogs.com/svg.image?\Gamma^{\hspace{2&space;mm}&space;\mu}_{\nu&space;\hspace{2&space;mm}&space;\rho}&space;=&space;\frac{1}{2}g^{\mu&space;\lambda}(\partial_{\nu}g_{\lambda&space;\rho}&space;&plus;&space;\partial_{\rho}g_{\lambda&space;\nu}&space;-&space;\partial_{\lambda}g_{\nu&space;\rho})&space;" title="\Gamma^{\hspace{2 mm} \mu}_{\nu \hspace{2 mm} \rho} = \frac{1}{2}g^{\mu \lambda}(\partial_{\nu}g_{\lambda \rho} + \partial_{\rho}g_{\lambda \nu} - \partial_{\lambda}g_{\nu \rho}) " />

In "geodetica sfera.nb" the geodesic on a sphere, which we know to be the circle of maximum radius, is calculated by solving the equation of motion:

<img src="https://latex.codecogs.com/svg.image?\frac{\partial^2&space;x^{\mu}}{\partial&space;\lambda^2}&plus;\Gamma^{\hspace{2&space;mm}&space;\mu}_{\nu&space;\hspace{2&space;mm}&space;\rho}\frac{\partial&space;x^{\nu}}{\partial&space;\lambda}\frac{\partial&space;x^{\rho}}{\partial&space;\lambda}&space;=&space;0&space;" title="\frac{\partial^2 x^{\mu}}{\partial \lambda^2}+\Gamma^{\hspace{2 mm} \mu}_{\nu \hspace{2 mm} \rho}\frac{\partial x^{\nu}}{\partial \lambda}\frac{\partial x^{\rho}}{\partial \lambda} = 0 " />

In "E-F_coor.py" the radial trajectories of light are considered in coordinates that solve the apparent singularity in rs = 2M. From the Schawrzchild metric it is obtained:

<img src="https://latex.codecogs.com/svg.image?\\ds^2&space;=&space;0&space;\Rightarrow&space;\frac{dr}{dx^0}&space;=&space;&space;\pm&space;\frac{r-r_s}{r}&space;\\r&space;&plus;&space;r_s&space;\ln(r-r_s)&space;=&space;\pm&space;x^0&space;&plus;&space;cost&space;" title="\\ds^2 = 0 \Rightarrow \frac{dr}{dx^0} = \pm \frac{r-r_s}{r} \\r + r_s \ln(r-r_s) = \pm x^0 + cost " />

where the + sign identifies the outgoing trajectories and the - the incoming ones

we can define:

<img src="https://latex.codecogs.com/svg.image?\\\begin{cases}v&space;=&space;x^0&space;&plus;&space;r&space;&plus;&space;r_s&space;\ln(r-r_s)&space;\\&space;r&space;=&space;r&space;\\\end{cases}&space;\\\\\text{and&space;in&space;this&space;coordinates:}\\\\ds^2&space;=&space;\Bigl(1&space;-&space;\frac{r_s}{r}\Bigr)dv^2&space;-&space;2dvdr&space;\\&space;\\\text{therefore&space;there&space;are&space;only&space;outgoing&space;trajectories.&space;in&space;the&space;code&space;the&space;coordinates&space;are&space;used:}\\\begin{cases}\overline{x^0}&space;=&space;v&space;-&space;r&space;\\&space;r&space;=&space;r&space;\\\end{cases}&space;" title="\\\begin{cases}v = x^0 + r + r_s \ln(r-r_s) \\ r = r \\\end{cases} \\\\\text{and in this coordinates:}\\\\ds^2 = \Bigl(1 - \frac{r_s}{r}\Bigr)dv^2 - 2dvdr \\ \\\text{therefore there are only outgoing trajectories. in the code the coordinates are used:}\\\begin{cases}\overline{x^0} = v - r \\ r = r \\\end{cases} " />


