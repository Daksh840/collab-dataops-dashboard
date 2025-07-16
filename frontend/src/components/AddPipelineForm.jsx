// src/components/AddPipelineForm.jsx
import React, { useState } from "react";

const AddPipelineForm = ({ onPipelineAdded }) => {
  const [formData, setFormData] = useState({
    name: "",
    status: "running",
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch("http://localhost:8000/pipelines", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        ...formData,
        last_updated: new Date().toISOString(),
      }),
    });

    if (response.ok) {
      const data = await response.json();
      onPipelineAdded(data.pipeline);
      setFormData({ name: "", status: "running" });
    } else {
      alert("Failed to add pipeline");
    }
  };

  return (
    <form onSubmit={handleSubmit} className="mb-6 p-4 bg-gray-800 rounded-lg shadow">
      <h2 className="text-lg font-semibold mb-4 text-white">Add New Pipeline</h2>
      <div className="mb-4">
        <input
          type="text"
          name="name"
          placeholder="Pipeline Name"
          value={formData.name}
          onChange={handleChange}
          className="w-full p-2 rounded bg-gray-900 text-white border border-gray-600"
          required
        />
      </div>
      <div className="mb-4">
        <select
          name="status"
          value={formData.status}
          onChange={handleChange}
          className="w-full p-2 rounded bg-gray-900 text-white border border-gray-600"
        >
          <option value="running">Running</option>
          <option value="paused">Paused</option>
          <option value="error">Error</option>
        </select>
      </div>
      <button
        type="submit"
        className="px-4 py-2 bg-purple-600 hover:bg-purple-700 text-white rounded"
      >
        Add Pipeline
      </button>
    </form>
  );
};

export default AddPipelineForm;
