import React, { useState, useEffect } from 'react';

export default function App() {
  const [activeTab, setActiveTab] = useState("chat");
  const [status, setStatus] = useState(null);

  useEffect(() => {
    fetch('/api/health')
      .then(res => res.json())
      .then(data => setStatus(data))
      .catch(err => console.error("Health check error:", err));
  }, []);

  return (
    <div className="flex flex-col min-h-screen bg-slate-50 text-slate-900 font-sans">
      <header className="bg-white border-b border-slate-200 sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex justify-between items-center h-16">
          <div className="flex items-center space-x-3">
            <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-blue-700 to-indigo-600 flex items-center justify-center text-white shadow-md">
              🎓
            </div>
            <div>
              <div className="flex items-center space-x-2">
                <span className="font-extrabold text-xl tracking-tight text-slate-900">CampusMitra</span>
                <span className="bg-blue-100 text-blue-700 text-xs px-2 py-0.5 rounded-full font-bold">AI</span>
              </div>
              <p className="text-xs text-slate-500">Indian Campus Concierge · ASI:One Protocol</p>
            </div>
          </div>

          <div className="flex space-x-2">
            <span className="px-2.5 py-1 rounded-full text-xs font-medium bg-emerald-100 text-emerald-800">
              ● Agentverse Online
            </span>
            <span className="px-2.5 py-1 rounded-full text-xs font-medium bg-indigo-100 text-indigo-800">
              ChromaDB RAG
            </span>
          </div>
        </div>
      </header>

      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6">
        <div className="bg-white p-8 rounded-2xl border border-slate-200 shadow-sm text-center">
          <h2 className="text-2xl font-bold text-slate-900">Welcome to CampusMitra AI</h2>
          <p className="text-sm text-slate-500 mt-2">
            FastAPI Backend + ChromaDB Vector RAG + LangGraph Multi-Agent Orchestrator + Fetch.ai uAgent
          </p>
          <div className="mt-6 flex justify-center space-x-4">
            <a href="/" className="bg-blue-600 hover:bg-blue-700 text-white font-semibold text-sm px-6 py-2.5 rounded-xl shadow-md transition">
              Open Interactive Concierge
            </a>
          </div>
        </div>
      </main>

      <footer className="bg-white border-t border-slate-200 py-4 text-center text-xs text-slate-500">
        CampusMitra AI · Built with React + Tailwind CSS + FastAPI + ChromaDB
      </footer>
    </div>
  );
}
