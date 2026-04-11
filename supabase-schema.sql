create extension if not exists pgcrypto;

create table if not exists public.bookings (
  id uuid primary key default gen_random_uuid(),
  created_at timestamptz not null default now(),
  name text not null,
  email text not null,
  country text not null,
  instagram_handle text,
  timezone text,
  question text not null,
  spread text not null,
  depth text not null,
  addons jsonb not null default '[]'::jsonb,
  total_price numeric(10,2) not null check (total_price >= 0),
  currency text not null check (currency in ('USD', 'INR')),
  status text not null default 'pending' check (status in ('pending', 'paid', 'reading_done', 'delivered')),
  delivery_method text not null default 'email_pdf',
  admin_email text not null default 'yvlostartarot@gmail.com'
);

alter table public.bookings enable row level security;

create policy "public can insert bookings"
on public.bookings
for insert
to anon, authenticated
with check (true);
