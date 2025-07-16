// src/App.js
import React, { useEffect, useState } from "react";
import { fetchPipelines } from "./api";
import Hyperspeed from "./components/Hyperspeed";
import MagicBento from "./components/MagicBento";
import AddPipelineForm from "./components/AddPipelineForm";

function App() {
  const [pipelines, setPipelines] = useState([]);

  useEffect(() => {
    const loadPipelines = async () => {
      const data = await fetchPipelines();
      setPipelines(data);
    };
    loadPipelines();
  }, []);

  const formatDate = (isoString) => {
    const date = new Date(isoString);
    return date.toLocaleString("en-IN", {
      dateStyle: "medium",
      timeStyle: "short",
    });
  };
  const handlePipelineAdded = (newPipeline) => {
    setPipelines((prev) => [...prev, newPipeline]);
  };


  return (
    <div className="relative min-h-screen text-white overflow-x-hidden overflow-y-auto">
      {/* Animated background */}
      <Hyperspeed />

      {/* Foreground overlay */}
      <div className="absolute inset-0 z-10 bg-black/50 backdrop-blur-sm px-4 sm:px-8 py-8">
        <h1 className="text-3xl font-bold mb-8 text-center text-white drop-shadow-lg">
          🚀 Collaborative Data-Ops Dashboard
        </h1>
        
        <AddPipelineForm onPipelineAdded={handlePipelineAdded} />
        {/* Magic Bento Cards with dynamic pipelines */}
        <MagicBento pipelines={pipelines} setPipelines={setPipelines} formatDate={formatDate} />
      </div>
    </div>
  );
}

export default App;
