import React, { useState } from 'react';
import api from '../services/api';

export default function EstimateForm() {
  const [form, setForm] = useState({
    shape: 'slab',
    length: '', width: '', height: '', diameter: '', quantity: 1,
    psi: 3000, airEntrained: false, placement: 'pump', wasteFactor: 0.05,
    temp: '', humidity: '', rain: '', distance: ''
  });
  const [result, setResult] = useState(null);

  const handleChange = e => {
    const { name, value, type, checked } = e.target;
    setForm(prev => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value
    }));
  };

  const handleSubmit = async e => {
    e.preventDefault();
    const payload = {
      shape: form.shape,
      dimensions: {
        length: parseFloat(form.length),
        width: form.shape !== 'round_column' ? parseFloat(form.width) : undefined,
        height: parseFloat(form.height),
        diameter: form.shape === 'round_column' ? parseFloat(form.diameter) : undefined
      },
      quantity: parseInt(form.quantity),
      mix: {
        psi: parseInt(form.psi),
        air_entrained: form.airEntrained,
        placement: form.placement,
        waste_factor: parseFloat(form.wasteFactor)
      },
      conditions: {
        ambient_temperature: parseFloat(form.temp),
        humidity: parseFloat(form.humidity),
        rain_last_24h: parseFloat(form.rain),
        plant_distance_miles: parseFloat(form.distance)
      }
    };
    const res = await api.post('/estimate', payload);
    setResult(res.data);
  };

  return (
    <div>
      <form onSubmit={handleSubmit} className="space-y-4">
        {/* Form inputs omitted for brevity; include fields for each form.prop */}
        <button type="submit" className="px-4 py-2 bg-blue-600 text-white rounded">
          Calculate
        </button>
      </form>
      {result && (
        <div className="mt-6 p-4 bg-white shadow">
          <h2 className="text-xl font-semibold">Results</h2>
          <p>Volume: {result.volume_cubic_yards} yd³</p>
          <p>With Waste: {result.volume_including_waste} yd³</p>
          <ul>
            {result.admixture_recommendations.map((r,i) => <li key={i}>{r}</li>)}
          </ul>
        </div>
      )}
    </div>
  );
}
