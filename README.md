# LangGraph Exercise - Graph V: Loop Structure

A LangGraph implementation demonstrating looping behavior with conditional self-referencing edges.

## Overview

This graph demonstrates how to create a loop structure in LangGraph where a node can conditionally route back to itself multiple times before proceeding to the end.

## Graph Structure
START → Greeting Node → Random Node ⟲ (loop back to itself) → END

### Flow Diagram
<img width="652" height="548" alt="image" src="https://github.com/user-attachments/assets/21809f1a-9769-4c4e-ab7b-3c56750fec08" />


## Nodes

- **greeting_node**: Entry node that initializes the conversation and sets up loop counter
- **random_node**: Processing node that executes repeatedly based on loop condition

# LangGraph Looping Example

A simple demonstration of **looping in LangGraph** using a conditional edge. This project shows how to build a graph that runs a node multiple times (5 loops) before ending.

This example is based on the **Looping.ipynb** notebook from the LangGraph Course.

---

## 📌 Overview

This project demonstrates:
- How to define a shared `AgentState`
- Creating nodes (Greeting + Random)
- Using **conditional edges** to create loops
- Using `Annotated` + `operator.add` for automatic list accumulation
- Building and compiling a LangGraph workflow

---

## ✨ Features

- Runs `random_node` exactly **5 times**
- Collects random numbers (0–10) in a list
- Clean separation of nodes and decision logic
- Easy to understand and extend

---

## 🛠️ Technologies Used

- Python 3.8+
- [LangGraph](https://www.langchain.com/langgraph)
- TypedDict with Annotations

---



Install required dependencies:
pip install langgraph
