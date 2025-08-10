export default function BalanceDisplay({ balance, loading, error }) {
  if (loading) return <p>Cargando saldo...</p>;
  if (error) return <p>{error}</p>;
  return <p>Saldo: ${balance.toFixed(2)}</p>;
}
