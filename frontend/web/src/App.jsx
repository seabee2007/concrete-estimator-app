
// frontend/web/src/App.jsx
import React from 'react';
import EstimateForm from './components/EstimateForm';

function App() {
  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <header className="mb-8">
        <h1 className="text-3xl font-bold">Concrete Estimator</h1>
      </header>
      <EstimateForm />
    </div>
  );
}

export default App;
