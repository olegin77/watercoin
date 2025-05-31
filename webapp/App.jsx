
import { useEffect, useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

export default function WatercoinWebApp() {
  const [user, setUser] = useState(null);
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchData() {
      const res = await fetch("/api/me");
      const data = await res.json();
      setUser(data);

      const h = await fetch("/api/history");
      setHistory(await h.json());
      setLoading(false);
    }
    fetchData();
  }, []);

  const claim = async () => {
    await fetch("/api/claim", { method: "POST" });
    alert("✅ Токены выданы!");
  };

  const withdraw = async () => {
    await fetch("/api/withdraw", { method: "POST" });
    alert("💸 Вывод выполнен!");
  };

  if (loading || !user) return <div className="p-4">Загрузка...</div>;

  return (
    <div className="p-4 space-y-4">
      <Card>
        <CardContent className="space-y-2">
          <h2 className="text-xl font-bold">Добро пожаловать, {user.username}</h2>
          <p>🪙 Адрес: {user.wallet}</p>
          <p>💧 Стейк: {user.stake} $WATER</p>
          <p>💰 Доход: {user.income} USDT</p>
        </CardContent>
      </Card>

      <Card>
        <CardContent>
          <h3 className="text-lg font-semibold mb-2">📈 Доходность AI</h3>
          <ResponsiveContainer width="100%" height={200}>
            <BarChart data={history}>
              <XAxis dataKey="date" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="profit" fill="#22d3ee" />
            </BarChart>
          </ResponsiveContainer>
        </CardContent>
      </Card>

      <div className="flex gap-2">
        <Button onClick={claim}>🎁 Получить токены</Button>
        <Button onClick={withdraw}>💸 Вывод</Button>
      </div>
    </div>
  );
}
