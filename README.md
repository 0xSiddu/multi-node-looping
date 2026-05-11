# LangGraph Exercise - Graph V: Loop Structure

A LangGraph implementation demonstrating looping behavior with conditional self-referencing edges.

## Overview

This graph demonstrates how to create a loop structure in LangGraph where a node can conditionally route back to itself multiple times before proceeding to the end.

## Graph Structure
START → Greeting Node → Random Node ⟲ (loop back to itself) → END

### Flow Diagram
┌─────────┐
│  START  │
└────┬────┘
│
▼
┌──────────────┐
│ Greeting Node│
└──────┬───────┘
│
▼
┌──────────────┐ ◄─────┐
│ Random Node  │       │
└──────┬───────┘       │
│               │
Condition          │
│               │
Loop? ──────────────┘
│
End
│
▼
┌──────────┐
│   END    │
└──────────┘

## Nodes

- **greeting_node**: Entry node that initializes the conversation and sets up loop counter
- **random_node**: Processing node that executes repeatedly based on loop condition

## Conditional Logic

The `should_continue()` function determines routing:
- **Returns "loop"**: Routes back to `random_node` (continues looping)
- **Returns "end"**: Routes to `END` (exits loop)

### Loop Condition
```python
if loop_count < max_loops:
    return "loop"  # Continue
else:
    return "end"   # Stop
```

## Installation

```bash
pip install langgraph
```

## Usage

```python
python graph_v.py
```

### Example Input

```python
initial_state = AgentState(
    message="",
    loop_count=0,
    max_loops=3  # Will loop 3 times
)
```

### Expected Output
Greeting Node: Hello! Starting the random loop process...
Random Node: Loop iteration 1/3
Decision: Continue looping (1/3)
Random Node: Loop iteration 2/3
Decision: Continue looping (2/3)
Random Node: Loop iteration 3/3
Decision: Max loops reached (3/3), ending...
Final Result:
Total loops executed: 3
Final message: Processing random operation - iteration 3

## State Structure

| Field | Type | Description |
|-------|------|-------------|
| `message` | str | Status message updated during processing |
| `loop_count` | int | Current iteration count |
| `max_loops` | int | Maximum number of loops before ending |

## Key Features

- ✅ Self-referencing loop structure
- ✅ Conditional routing (loop or end)
- ✅ Configurable loop count
- ✅ State tracking across iterations
- ✅ Clean loop exit condition

## Use Cases

This pattern is useful for:
- Retry logic with maximum attempts
- Iterative processing until condition met
- Polling operations
- Batch processing with iteration limits
- State machines with repeating states

## Customization

### Change Loop Count
```python
initial_state = AgentState(
    message="",
    loop_count=0,
    max_loops=10  # Loop 10 times instead
)
```

### Add Random Exit Condition
```python
import random

def should_continue(state: AgentState) -> str:
    # Exit randomly or after max loops
    if state['loop_count'] < state['max_loops'] and random.random() > 0.3:
        return "loop"
    return "end"
```

### Add More Processing
```python
def random_node(state: AgentState) -> AgentState:
    state['loop_count'] += 1
    # Add your custom processing here
    result = perform_some_operation()
    state['message'] = f"Result: {result}"
    return state
```


## Notes

- The loop structure uses conditional edges with self-reference
- Loop counter prevents infinite loops
- State persists across all loop iterations
- Clean separation between loop logic and exit logic
