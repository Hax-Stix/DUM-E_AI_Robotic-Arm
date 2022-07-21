import math

#Varibles

#Time
T = ?

#Force Motor
F_MW = ?
F_ME = ?
F_MS = ?

#Gravity
G = 9.81

#Mass
M_W = ?
M_E = ?
M_S = 
#Mass Total
M_T = ?

#Radius
R_W = ?
R_E = ?
R_S = ?
#Multi Radius
R_WE = ?
R_ES = ?
R_WS = ?

#Angles
A_W = ?
A_E = ?
A_E_1 = ?
A_E_2 = ?
A_S = ?
A_S_1 = ?
A_S_2 = ?

#Torques
Tr_W = ?
Tr_E = ?
Tr_S = ?
#Torque Total
Tr_T = ?

#Lengths
L_W = ?
L_E = ?
L_S = ?


#Basic Formulaes
#Force = Mass * Gravity
#F? = M? * G
#Torque = Force * Radius
#Tr? = F? * R?
#Find UnKnown Length of Iregular Triangle
#L1^2 = L2^2 + L3^2 -((2)(L2)(L3)(math.cos(A1)))
#Find UnKnown Angle of Iregular Triangle
#math.cos(A1) = (L2^2 + L3^2 - L1^2)/((2)(L2)(L3))


#Find Torques On Each Individual Joint
Tr_W = (M_W * 9.81) * L_W
Tr_E = ((M_W * 9.81) * (math.sqrt(L_W^2 + L_E^2 -(((2) * (L_W) * (L_E)) * (math.cos(A_W)))))) + ((M_E * 9.81) * L_E)
Tr_S = (M_W * 9.81) * (math.sqrt((math.sqrt(L_W^2 + L_E^2 -(((2) * (L_W) * (L_E)) * (math.cos(A_W)))))^2 + L_S^2 -(((2) * ((math.sqrt(L_W^2 + L_E^2 -(((2) * (L_W) * (L_E)) * (math.cos(A_W)))))) * (L_S)) * (math.cos((A_E - (math.acos(((math.sqrt(L_W^2 + L_E^2 -(((2) * (L_W) * (L_E)) * (math.cos(A_W)))))^2 + L_E^2 - L_W^2)/((2)((math.sqrt(L_W^2 + L_E^2 -(((2) * (L_W) * (L_E)) * (math.cos(A_W))))))(L_E)))))))))) + ((M_E * 9.81) * (math.sqrt(L_E^2 + L_S^2 -(((2) * (L_E) * (L_S)) * (math.cos(A_E)))))) + ((M_S * 9.81) * L_S)

Tr_S = ((M_W * 9.81) * R_WS) + ((M_E * 9.81) * R_WE) + ((M_S * 9.81) * R_S)
R_WE = (math.sqrt(L_W^2 + L_E^2 -(((2) * (L_W) * (L_E)) * (math.cos(A_W)))))
A_E_1 = (math.acos((R_WE^2 + L_E^2 - L_W^2)/((2)(R_WE)(L_E))))
A_E_2 = (A_E - A_E_1)
R_WS = (math.sqrt(R_WE^2 + L_S^2 -((2)*(R_WE)*(L_S)(math.cos(A_E_2)))))

R_WS??? = (math.sqrt((math.sqrt(L_W^2 + L_E^2 -(((2) * (L_W) * (L_E)) * (math.cos(A_W)))))^2 + L_S^2 -(((2) * ((math.sqrt(L_W^2 + L_E^2 -(((2) * (L_W) * (L_E)) * (math.cos(A_W)))))) * (L_S)) * (math.cos((A_E - (math.acos(((math.sqrt(L_W^2 + L_E^2 -(((2) * (L_W) * (L_E)) * (math.cos(A_W)))))^2 + L_E^2 - L_W^2)/((2)((math.sqrt(L_W^2 + L_E^2 -(((2) * (L_W) * (L_E)) * (math.cos(A_W))))))(L_E))))))))))