from langgraph.graph import StateGraph, END
from typing import TypedDict
import random

# Define the state structure
class AgentState(TypedDict):
    message: str
    loop_count: int
    max_loops: int

# Define the nodes
def greeting_node(state: AgentState) -> AgentState:
    """Greeting node that initializes the conversation"""
    print("Greeting Node: Hello! Starting the random loop process...")
    state['message'] = "Hello from Greeting Node"
    state['loop_count'] = 0
    return state

def random_node(state: AgentState) -> AgentState:
    """Random node that processes and increments loop count"""
    state['loop_count'] += 1
    print(f"Random Node: Loop iteration {state['loop_count']}/{state['max_loops']}")
    state['message'] = f"Processing random operation - iteration {state['loop_count']}"
    return state

# Conditional function to decide whether to loop or end
def should_continue(state: AgentState) -> str:
    """
    Determines whether to loop back to random_node or end
    Returns 'loop' to continue, 'end' to finish
    """
    if state['loop_count'] < state['max_loops']:
        print(f"Decision: Continue looping ({state['loop_count']}/{state['max_loops']})")
        return "loop"
    else:
        print(f"Decision: Max loops reached ({state['loop_count']}/{state['max_loops']}), ending...")
        return "end"

# Build the graph
workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("greeting_node", greeting_node)
workflow.add_node("random_node", random_node)

# Set entry point
workflow.set_entry_point("greeting_node")

# Add edge from greeting to random
workflow.add_edge("greeting_node", "random_node")

# Add conditional edges from random_node
workflow.add_conditional_edges(
    "random_node",
    should_continue,
    {
        "loop": "random_node",  # Loop back to itself
        "end": END              # Go to END
    }
)

# Compile the graph
app = workflow.compile()

# Test the graph
if __name__ == "__main__":
    # Example 1: Loop 3 times
    print("=" * 60)
    print("Example 1: Running with max_loops=3")
    print("=" * 60)
    
    initial_state = AgentState(
        message="",
        loop_count=0,
        max_loops=3
    )
    
    result = app.invoke(initial_state)
    
    print("=" * 60)
    print("Final Result:")
    print(f"Total loops executed: {result['loop_count']}")
    print(f"Final message: {result['message']}")
    print("=" * 60)
    
    # Example 2: Loop 5 times
    print("\n" + "=" * 60)
    print("Example 2: Running with max_loops=5")
    print("=" * 60)
    
    initial_state2 = AgentState(
        message="",
        loop_count=0,
        max_loops=5
    )
    
    result2 = app.invoke(initial_state2)
    
    print("=" * 60)
    print("Final Result:")
    print(f"Total loops executed: {result2['loop_count']}")
    print(f"Final message: {result2['message']}")
    print("=" * 60)
