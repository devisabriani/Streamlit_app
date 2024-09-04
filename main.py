import React, { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Select, SelectTrigger, SelectValue, SelectContent, SelectItem } from '@/components/ui/select';
import { Card, CardContent, CardHeader } from '@/components/ui/card';

export default function StreamlitSimulation() {
  const [topic, setTopic] = useState('');
  const [grade, setGrade] = useState('');
  const [result, setResult] = useState('');

  const handlePlan = () => {
    if (topic && grade) {
      setResult('Pianificazione completata! Qui verrebbe mostrato il risultato della pianificazione.');
    }
  };

  return (
    <div className="max-w-2xl mx-auto p-4 bg-gray-100 rounded-lg shadow">
      <h1 className="text-2xl font-bold mb-4 text-center">Pianificatore di Lezioni con CrewAI</h1>
      <Input
        type="text"
        placeholder="Inserisci l'argomento della lezione"
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
        className="mb-4"
      />
      <Select value={grade} onValueChange={setGrade}>
        <SelectTrigger className="mb-4 w-full">
          <SelectValue placeholder="Seleziona la classe" />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="Elementari">Elementari</SelectItem>
          <SelectItem value="Medie">Medie</SelectItem>
          <SelectItem value="Superiori">Superiori</SelectItem>
        </SelectContent>
      </Select>
      <Button onClick={handlePlan} className="w-full mb-4">
        Pianifica Lezione
      </Button>
      {result && (
        <Card>
          <CardHeader>Risultato</CardHeader>
          <CardContent>{result}</CardContent>
        </Card>
      )}
    </div>
  );
}
