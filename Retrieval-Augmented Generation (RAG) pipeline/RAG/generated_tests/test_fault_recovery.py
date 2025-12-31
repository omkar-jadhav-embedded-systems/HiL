In this example, I'll provide PyTest test case skeletons for an embedded controller that focuses on boundary conditions, negative cases, and timing behavior based on the provided requirement context.

```python
import pytest
from unittest.mock import Mock, patch

def test_controller_normal_state_after_fault():
    # Arrange
    faulty_controller = FaultyController()  # Placeholder class for controller
    clear_fault_function = Mock(return_value=None)  # Placeholder function to clear fault
    set_normal_state_function = Mock()  # Placeholder function to set the normal state

    # Assuming that FaultyController has a method `set_fault` and attributes `normal_state`, `is_faulted`
    faulty_controller.normal_state = 'NORMAL'
    faulty_controller.is_faulted = True

    with patch.object(faulty_controller, 'clear_fault', new=clear_fault_function) as clear_fault:
        with patch.object(faulty_controller, 'set_normal_state', new=set_normal_state_function) as set_normal_state:
            # Act
            clear_fault.delay = 101  # Simulate failure to recover in the expected time (101ms)
            faulty_controller.clear_fault()

            clear_fault.delay = 99  # Simulate successful recovery in the expected time (99ms)
            faulty_controller.clear_fault()

    # Assert
    assert faulty_controller.normal_state == 'NORMAL'  # Check if controller enters NORMAL state after clearing fault
    set_normal_state.assert_has_calls([call()])  # Verify that `set_normal_state` is called when controller recovers

def test_controller_recovery_timing():
    # Arrange
    controller = NormalController()  # Placeholder class for normal controller
    clear_fault_function = Mock(return_value=None)  # Placeholder function to clear fault
    set_normal_state_function = Mock()  # Placeholder function to set the normal state

    with patch.object(controller, 'clear_fault', new=clear_fault_function) as clear_fault:
        with patch.object(controller, 'set_normal_state', new=set_normal_state_function) as set_normal_state:
            # Act (Test recovery time between 50ms and 150ms)
            for i in range(50, 151):
                clear_fault.delay = i
                controller.clear_fault()

    # Assert
    recovered_times = [call().delay for call in set_normal_state.call_args_list]
    assert 50 <= min(recovered_times) <= 100 <= max(recovered_times) <= 150  # Check if controller recovers within the expected time (50ms-150ms)

def test_controller_negative():
    # Arrange
    faulty_controller = FaultyController()

    with patch.object(faulty_controller, 'clear_fault', side_effect=ValueError("Unexpected error")):
        # Act and Assert
        with pytest.raises(ValueError):
            faulty_controller.clear_fault()  # Test if an unexpected error raises a ValueError
```

These test cases cover boundary conditions, negative cases, and timing behavior for the given requirement context. However, it is essential to implement concrete classes or functions for the controller and its methods as placeholders in this example.