import React, { useEffect, useState } from "react";

const App = () => {
  const [isOpenForm, setIsOpenForm] = useState(false);
  const [enteredText, setEnteredText] = useState("");
  const [todos, setTodos] = useState([]);

  async function fetchTodos() {
    try {
      const response = await fetch("http://localhost:8000/api/list/");
      const data = await response.json();
      console.log("Fetched todos:", data);
      if (response.status === 200) {
        setTodos(data);
      }
    } catch (error) {
      console.error("Error fetching todos:", error);
    }
  }

  useEffect(() => {
    fetchTodos();
  }, []);

  function toggleForm() {
    setIsOpenForm((prevState) => !prevState);
  }

  async function submitTaskHandler() {
    try {
      const response = await fetch("http://localhost:8000/api/list/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ task: enteredText }),
      });
      if (response.status === 201 || response.status === 200) {
        const newTask = await response.json();
        setTodos((prevState) => [...prevState, newTask]);
        setEnteredText("");
      }
    } catch (error) {
      console.log("Error submitting task:", error);
    }
  }

  async function deleteTask(id) {
    try {
      const response = await fetch(`http://localhost:8000/api/detail/${id}/`, {
        method: "DELETE",
      });
      if (response.status === 204 || response.status === 200) {
        setTodos((prevState) => prevState.filter((todo) => todo.id !== id));
      }
      else{
        console.log("Failed to delete task. Status code:", response.status);
      }
    } catch (error) {
      console.log("Error deleting task:", error);
    }
  }

  return (
    <div className="container mt-5">
      <div className="d-flex justify-content-center mt-4">
        <div className="col-md-5 p-2">
          {/* Add todo section */}
          <div className="d-flex justify-content-between p-2 shadow rounded">
            <h2>Todo app</h2>
            <button onClick={toggleForm} className="btn btn-info">
              Add Todo
            </button>
          </div>
          {isOpenForm && (
            <div className="p-2 shadow my-2 rounded">
              <div className="d-flex gap-2">
                <input
                  type="text"
                  placeholder="Enter a task..."
                  className="form-control"
                  value={enteredText}
                  onChange={(e) => setEnteredText(e.target.value)}
                />
                <button onClick={submitTaskHandler} className="btn btn-success">
                  Save
                </button>
              </div>
            </div>
          )}
          <div className="p-2 my-4">
            {todos.length > 0 ? (
              <ul className="list-unstyled">
                {todos.map((todo) => (
                  <li
                    key={todo.id}
                    className="d-flex justify-content-between align-items-center shadow p-2 rounded"
                  >
                    <div className="d-flex align-items-center gap-2">
                      {/* todo content */}
                      <span>{todo.task}</span>
                    </div>

                    {/* delete and edit button */}
                    <div className="d-flex gap-2">
                      <button className="btn btn-primary">Edit</button>
                      <button
                        className="btn btn-danger"
                        onClick={() => deleteTask(todo.id)}
                      >
                        Delete
                      </button>
                    </div>
                  </li>
                ))}
              </ul>
            ) : (
              <p className="text-center">No tasks added yet.</p>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default App;
