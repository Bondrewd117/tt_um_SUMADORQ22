import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles
from cocotb.result import TestFailure
import random

clk_r = 100  # 100 ns = 10 MHz

def signed_format(value):
    sign = 1 if value < 0 else 0
    magnitude = abs(value) & 0b1111
    return (sign << 4) | magnitude 

def decode_siii(encoded):
    sign = -1 if (encoded >> 5) & 0x1 else 1
    magnitude = encoded & 0b11111  # 5 bits de magnitud
    return sign * magnitude


@cocotb.test()
async def test_sumador_a_0(dut):
# Inicialización
    dut._log.info("Iniciando testbench")
    
    # Configuración del reloj
    clock = Clock(dut.clk, clk_r, units="ns")
    cocotb.start_soon(clock.start())

    # Reset sequence
    dut._log.info("Aplicando reset")
    dut.ena.value = 1
    dut.uio_out.value = 0
    dut.rst_n.value = 0  # Reset activo bajo
    

    await ClockCycles(dut.clk, 1)  # Mantener reset por 5 ciclos
    dut.rst_n.value = 1  # Liberar reset
    await ClockCycles(dut.clk, 1)  # Ciclo adicional después del reset

    dut.rst_n.value = 0  # Liberar reset
    await ClockCycles(dut.clk, 1)  # Ciclo adicional después del reset
    
    # Valores de prueba
    input_a = 0
    input_b = random.randint(0,15)
    
    # Asignar entradas (nota: en el testbench Verilog, ui_in = a[4:0] y uio_in = b[4:0])
    dut.ui_in.value = input_a & 0x1F  # Asegurar 5 bits (0-4)
    dut.uio_in.value = input_b & 0x1F  # Asegurar 5 bits (0-4)

    # Esperar suficiente tiempo para la propagación
    await ClockCycles(dut.clk, 5)  # Esperar 1 ciclos de reloj

    # Verificación
    expected_output = input_b  # Según tu requerimiento
    observed_output = decode_siii(dut.uo_out.value.integer)
    
    dut._log.info(f"a: {input_a} , b: {input_b}")
    dut._log.info(f"Salida observada: {observed_output} (0x{observed_output:02X}), Esperada: {expected_output}")
   
    if observed_output != expected_output:
        raise TestFailure(f"Error! Salida={observed_output}, Esperado={expected_output}")
    
    dut._log.info("¡Prueba exitosa!")

@cocotb.test()
async def test_sumador_b_0(dut):
    # Inicialización
    dut._log.info("Iniciando testbench")
    
    # Configuración del reloj
    clock = Clock(dut.clk, clk_r, units="ns")
    cocotb.start_soon(clock.start())

    # Reset sequence
    dut._log.info("Aplicando reset")
    dut.ena.value = 1
    dut.uio_out.value = 0
    dut.rst_n.value = 0  # Reset activo bajo
    

    await ClockCycles(dut.clk, 1)  # Mantener reset por 5 ciclos
    dut.rst_n.value = 1  # Liberar reset
    await ClockCycles(dut.clk, 1)  # Ciclo adicional después del reset

    dut.rst_n.value = 0  # Liberar reset
    await ClockCycles(dut.clk, 1)  # Ciclo adicional después del reset
    
    # Valores de prueba
    input_a = random.randint(0,15)
    input_b = 0
    
    # Asignar entradas (nota: en el testbench Verilog, ui_in = a[4:0] y uio_in = b[4:0])
    dut.ui_in.value = input_a & 0x1F  # Asegurar 5 bits (0-4)
    dut.uio_in.value = input_b & 0x1F  # Asegurar 5 bits (0-4)
    
    # Asignar entradas (nota: en el testbench Verilog, ui_in = a[4:0] y uio_in = b[4:0])
    dut.ui_in.value = input_a & 0x1F  # Asegurar 5 bits (0-4)
    dut.uio_in.value = input_b & 0x1F  # Asegurar 5 bits (0-4)
    
    # Esperar suficiente tiempo para la propagación
    await ClockCycles(dut.clk, 5)  # Esperar 1 ciclos de reloj

    # Verificación
    expected_output = input_a  # Según tu requerimiento
    observed_output = dut.uo_out.value.integer
    
    dut._log.info(f"a: {input_a} , b: {input_b}")
    dut._log.info(f"Salida observada: {observed_output} (0x{observed_output:02X}), Esperada: {expected_output}")
    
    if observed_output != expected_output:
        raise TestFailure(f"Error! Salida={observed_output}, Esperado={expected_output}")
    
    dut._log.info("¡Prueba exitosa!")

@cocotb.test()
async def test_sumador_add(dut):
    # Inicialización
    dut._log.info("Iniciando testbench")
    
    # Configuración del reloj
    clock = Clock(dut.clk, clk_r, units="ns")
    cocotb.start_soon(clock.start())

    # Reset sequence
    dut._log.info("Aplicando reset")
    dut.ena.value = 1
    dut.uio_out.value = 0
    dut.rst_n.value = 0  # Reset activo bajo


    await ClockCycles(dut.clk, 1)  # Mantener reset por 5 ciclos
    dut.rst_n.value = 1  # Liberar reset
    await ClockCycles(dut.clk, 1)  # Ciclo adicional después del reset

    dut.rst_n.value = 0  # Liberar reset
    await ClockCycles(dut.clk, 2)  # Ciclo adicional después del reset
    
    # Valores de prueba
    input_a = random.randint(0, 8)
    input_b = random.randint(0, 8)
    
    # Asignar entradas (nota: en el testbench Verilog, ui_in = a[4:0] y uio_in = b[4:0])
    dut.ui_in.value = input_a & 0x1F  # Asegurar 5 bits (0-4)
    dut.uio_in.value = input_b & 0x1F  # Asegurar 5 bits (0-4)

    # Asignar entradas (nota: en el testbench Verilog, ui_in = a[4:0] y uio_in = b[4:0])
    dut.ui_in.value = input_a & 0x1F  # Asegurar 5 bits (0-4)
    dut.uio_in.value = input_b & 0x1F  # Asegurar 5 bits (0-4)
    
    # Esperar suficiente tiempo para la propagación
    await ClockCycles(dut.clk, 5)  # Esperar 1 ciclos de reloj

    # Verificación
    expected_output = input_a + input_b # Según tu requerimiento
    observed_output = dut.uo_out.value.integer
    
    dut._log.info(f"a: {input_a} , b: {input_b}")
    dut._log.info(f"Salida observada: {observed_output} (0x{observed_output:02X}), Esperada: {expected_output}")
    
    if observed_output != expected_output:
        raise TestFailure(f"Error! Salida={observed_output}, Esperado={expected_output}")
    
    dut._log.info("¡Prueba exitosa!")


