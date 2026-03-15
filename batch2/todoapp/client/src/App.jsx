import React, { useState } from "react";

const App = () => {
  const [isOpenForm, setIsOpenForm] = useState(false);
  const [enteredText, setEnteredText] = useState("");
  const [todos, setTodos] = useState([
    {
      id: 1,
      task: "Learn Django for 20 minutes.",
      isCompleted: true,
    },
    {
      id: 2,
      task: "Run for 10 minutes.",
      isCompleted: false,
    },
    {
      id: 3,
      task: "Explore React.",
      isCompleted: false,
    },
    {
      id: 4,
      task: "Go and buy a coffee.",
      isCompleted: true,
    },
  ]);

  function toggleForm() {
    setIsOpenForm((prevState) => !prevState);
  }

  function submitTaskHandler() {
    setTodos((prevState) => [
      ...prevState,
      { id: Math.random(), task: enteredText, isCompleted: false },
    ]);
  }

  function deleteTask(id) {
    setTodos((prevState) => prevState.filter((todo) => todo.id !== id));
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
            <ul className="list-unstyled">
              {todos.map((todo) => (
                <li
                  key={todo.id}
                  className="d-flex justify-content-between align-items-center shadow p-2 rounded"
                >
                  <div className="d-flex align-items-center gap-2">
                    <input
                      type="checkbox"
                      className="form-check-input"
                      checked={todo.isCompleted && true}
                    />
                    {/* todo content */}
                    <span>{todo.task}</span>
                  </div>

                  {/* delete and edit button */}
                  <div className="d-flex gap-2">
                    <button className="btn btn-primary">Edit</button>
                    <button className="btn btn-danger" onClick={() => deleteTask(todo.id)}>Delete</button>
                  </div>
                </li>
              ))}
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
};

export default App;
