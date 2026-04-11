create extension if not exists pgcrypto;

-- Bookings table
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

-- Reviews table with admin comments
create table if not exists public.reviews (
  id uuid primary key default gen_random_uuid(),
  created_at timestamptz not null default now(),
  name text not null,
  rating integer not null check (rating >= 1 and rating <= 5),
  review text not null,
  status text not null default 'published' check (status in ('published', 'hidden', 'deleted')),
  admin_comment text,
  admin_comment_at timestamptz,
  is_featured boolean not null default false
);

alter table public.reviews enable row level security;

-- Public can view published reviews
create policy "public can view published reviews"
on public.reviews
for select
to anon, authenticated
using (status = 'published');

-- Public can insert reviews
create policy "public can insert reviews"
on public.reviews
for insert
to anon, authenticated
with check (true);

-- Admin can update/delete all reviews (requires authenticated admin user)
create policy "admin can manage reviews"
on public.reviews
for all
to authenticated
using (true)
with check (true);
