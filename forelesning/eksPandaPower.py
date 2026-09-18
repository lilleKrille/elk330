import pandapower as pp
import pandapower.plotting as plot
import matplotlib.pyplot as plt

# --------------------------------------------------
# Opprett nett
# --------------------------------------------------

net = pp.create_empty_network()

# --------------------------------------------------
# Busser
# --------------------------------------------------

b0 = pp.create_bus(
    net,
    vn_kv=0.4,
    name="Trafo",
    geodata=(0, 0)
)

b1 = pp.create_bus(
    net,
    vn_kv=0.4,
    name="Load",
    geodata=(1, 0)
)

b2 = pp.create_bus(
    net,
    vn_kv=0.4,
    name="PV",
    geodata=(2, 0)
)



# --------------------------------------------------
# Nettstasjon
# --------------------------------------------------

pp.create_ext_grid(net, b0)

# --------------------------------------------------
# Linjer
# --------------------------------------------------

line1 = pp.create_line_from_parameters(
    net,
    b0, b1,
    length_km=0.1,
    r_ohm_per_km=0.642,
    x_ohm_per_km=0.083,
    c_nf_per_km=0,
    max_i_ka=0.2
)

line2 = pp.create_line_from_parameters(
    net,
    b1, b2,
    length_km=0.1,
    r_ohm_per_km=0.642,
    x_ohm_per_km=0.083,
    c_nf_per_km=0,
    max_i_ka=0.2
)

# --------------------------------------------------
# Last
# --------------------------------------------------


# Last ved Bus1
pp.create_load(
    net,
    bus=b1,
    p_mw=0.050,   # 50 kW
    q_mvar=0.010,
    name="Load1"
)

# Last ved Bus2
pp.create_load(
    net,
    bus=b2,
    p_mw=0.015,   # 15 kW
    q_mvar=0.003,
    name="Load2"
)

# --------------------------------------------------
# PV-anlegg 44 kWp
# --------------------------------------------------

#pv = pp.create_sgen(
#    net,
#    bus=b2,
#    p_mw=0.021, #
#    q_mvar =0.11,
#    name="PV"
#)

# --------------------------------------------------
# Lastflyt
# --------------------------------------------------

pp.runpp(net, numba=False)

# --------------------------------------------------
# Resultater
# --------------------------------------------------

print("\nBus-spenninger")
print(net.res_bus.vm_pu)
print(net.res_bus[["vm_pu", "va_degree"]])
print("\nEffekt fra nettet")
print(net.res_ext_grid.p_mw)

print("\nEffektflyt i linjer")
print(net.res_line[["p_from_mw"]])

#print('nett',net.load)

# --------------------------------------------------
# Plott nett
# --------------------------------------------------

plt.figure(figsize=(8,3))

plot.simple_plot(
    net,
    bus_size=1,
    line_width=2,
    plot_loads=True,
    plot_sgens=True
)

plt.show()
