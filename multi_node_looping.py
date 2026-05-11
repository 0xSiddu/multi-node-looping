# ================================================
# LangGraph Looping Example (Single File)
# Based on Looping.ipynb from the course
# ================================================

from typing import TypedDict, Annotated
import operator
import random
from langgraph.graph import StateGraph, END

# ============================
# 1. Define the State
# ============================
class AgentState(TypedDict):
    name: str
    number: Annotated[list[int], operator.add]   # Allows automatic appending of lists
    counter: int


# ============================
# 2. Define the Nodes
# ============================

def greeting_node(state: AgentState) -> AgentState:
    """Greeting Node - Runs only once"""
    print("=== Greeting Node Executed ===")
    state["name"] = f"Hi there, {state['name']}!"
    state["counter"] = 0                    # Reset counter
    return state


def random_node(state: AgentState) -> AgentState:
    """Random Node - This node will loop 5 times"""
    random_num = random.randint(0, 10)
    state["number"].append(random_num)      # Add random number to list
    state["counter"] += 1                   # Increment counter
    
    print(f"Random Node: Generated number = {random_num} | Counter = {state['counter']}/5")
    return state


# ============================
# 3. Conditional Function (Decision Maker)
# ============================

def should_continue(state: AgentState) -> str:
    """Decides whether to continue looping or end"""
    if state["counter"] < 5:
        print(f"Decision: Continue looping... (Current count: {state['counter']})\n")
        return "loop"
    else:
        print("Decision: Max loops reached. Ending the graph.\n")
        return "exit"


# ============================
# 4. Build the Graph
# ============================

workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("greeting", greeting_node)
workflow.add_node("random", random_node)

# Set entry point
workflow.set_entry_point("greeting")

# Fixed edge: Greeting → Random
workflow.add_edge("greeting", "random")

# Conditional edges from random node
workflow.add_conditional_edges(
    "random",
    should_continue,
    {
        "loop": "random",   # Loop back to random node
        "exit": END         # End the workflow
    }
)

# Compile the graph
app = workflow.compile()


# ============================
# 5. Run the Graph
# ============================

if __name__ == "__main__":
    print("🚀 Starting LangGraph Looping Example\n")
    
    initial_state = {
        "name": "Vaibhav",
        "number": [],           # Empty list to collect random numbers
        "counter": 0
    }
    
    result = app.invoke(initial_state)
    
    print("=" * 50)
    print("✅ FINAL RESULT")
    print("=" * 50)
    print(f"Name    : {result['name']}")
    print(f"Numbers : {result['number']}")
    print(f"Counter : {result['counter']}")
    print("=" * 50)
