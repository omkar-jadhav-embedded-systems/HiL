Here is a PyTest test case skeleton that follows your requirements. Please note that this code does not actually interact with the embedded controller hardware, but it simulates the required scenarios using placeholders.

```python
import pytest

class TestEmbeddedController:
    def test_fault_state(self):
        # Placeholder for the embedded controller object
        controller = EmbeddedControllerPlaceholder()

        # Positive case - DC bus voltage within acceptable range
        controller.set_dc_bus_voltage(419)
        assert not controller.is_in_fault_state()

        # Boundary condition - DC bus voltage at the maximum limit
        controller.set_dc_bus_voltage(420)
        assert controller.is_in_fault_state()

        # Boundary condition - DC bus voltage slightly above the maximum limit
        controller.set_dc_bus_voltage(421)
        assert controller.is_in_fault_state()

        # Negative case - DC bus voltage below the minimum acceptable value
        controller.set_dc_bus_voltage(409)
        assert not controller.is_in_fault_state()

        # Testing fault state persistence over time (50ms+)
        time_start = pytest.time.monotonic()
        controller.set_dc_bus_voltage(420)
        time_elapsed = pytest.time.monotonic() - time_start

        # Here we assume that the fault state is only set after 50ms, you may need to adjust this value accordingly
        if time_elapsed > 0.05:
            assert controller.is_in_fault_state()
        else:
            assert not controller.is_in_fault_state()

    # Placeholder for the EmbeddedController class with is_in_fault_state and set_dc_bus_voltage methods
    class EmbeddedControllerPlaceholder:
        def __init__(self):
            self.fault_state = False
            self.dc_bus_voltage = 0

        def set_dc_bus_voltage(self, voltage):
            self.dc_bus_voltage = voltage

        def is_in_fault_state(self):
            return self.fault_state
```

This test case checks the expected behavior of the embedded controller when the DC bus voltage exceeds 420V continuously for more than 50ms. It uses boundary conditions, negative cases and timing behavior to ensure that the system correctly enters the FAULT state in the required scenarios.