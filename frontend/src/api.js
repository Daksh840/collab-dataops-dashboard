// src/api.js

import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000";

export const fetchPipelines = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/pipelines`);
    return response.data;
  } catch (error) {
    console.error("❌ Failed to fetch pipelines:", error);
    return [];
  }
};

export const deletePipeline = async (id) => {
  const response = await fetch(`http://localhost:8000/pipelines/${id}`, {
    method: "DELETE",
  });

  if (!response.ok) {
    throw new Error("Failed to delete pipeline");
  }

  return await response.json();
};
