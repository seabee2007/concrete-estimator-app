import React, { useState } from 'react';
import { View, TextInput, Button, Text, Switch } from 'react-native';
import api from '../services/api';

export default function EstimateScreen() {
  const [form, setForm] = useState({
    shape: 'slab', length: '', width: '', height: '', diameter: '', quantity: '1',
    psi: '3000', airEntrained: false, placement: 'pump', wasteFactor: '0.05',
    temp: '', humidity: '', rain: '', distance: ''
  });
  const [result, setResult] = useState(null);

  const handleChange = (name, value) => setForm(prev => ({ ...prev, [name]: value }));

  const handleSubmit = async () => {
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
    <View>
      {/* Similar inputs as web form using TextInput and Switch */}
      <Button title="Calculate" onPress={handleSubmit} />
      {result && (
        <View style={{ marginTop: 16 }}>
          <Text>Volume: {result.volume_cubic_yards} yd³</Text>
          <Text>With Waste: {result.volume_including_waste} yd³</Text>
          {result.admixture_recommendations.map((r, i) => <Text key={i}>{r}</Text>)}
        </View>
      )}
    </View>
  );
}
