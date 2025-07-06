import { useState } from "react"

export default function ReportForm() {
  const [data, setData] = useState({})

  const handleSubmit = async (e: any) => {
    e.preventDefault()
    const form = new FormData(e.target)
    const input = Object.fromEntries(form.entries())

    const res = await fetch("/api/builder/estimate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(input)
    })
    const result = await res.json()
    setData(result)
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <input name="land_cost" placeholder="Land Cost" required className="border p-2" />
      <input name="permit_cost" placeholder="Permit Cost" required className="border p-2" />
      <input name="construction_cost" placeholder="Construction Cost" required className="border p-2" />
      <input name="sale_price" placeholder="Sale Price" required className="border p-2" />
      <button type="submit" className="bg-blue-600 text-white p-2">Estimate</button>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </form>
  )
}