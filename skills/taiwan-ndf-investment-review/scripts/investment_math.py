#!/usr/bin/env python3
import argparse
import json


def safe_div(a, b):
    if a is None or b in (None, 0):
        return None
    return a / b


def main():
    p = argparse.ArgumentParser(description="Deterministic financing and EPS checks")
    p.add_argument("--investment", type=float)
    p.add_argument("--pre-money", type=float)
    p.add_argument("--post-money", type=float)
    p.add_argument("--investor-ownership", type=float, help="Decimal, e.g. 0.20")
    p.add_argument("--shares-before", type=float)
    p.add_argument("--share-price", type=float)
    p.add_argument("--net-income-current", type=float)
    p.add_argument("--net-income-forward", type=float)
    args = p.parse_args()

    inv = args.investment
    pre = args.pre_money
    post = args.post_money
    own = args.investor_ownership

    if post is None and pre is not None and inv is not None:
        post = pre + inv
    if pre is None and post is not None and inv is not None:
        pre = post - inv
    if post is None and inv is not None and own not in (None, 0):
        post = inv / own
    if pre is None and post is not None and inv is not None:
        pre = post - inv
    if own is None and inv is not None and post not in (None, 0):
        own = inv / post

    shares_new = None
    shares_after = None
    if inv is not None and args.share_price not in (None, 0):
        shares_new = inv / args.share_price
    if args.shares_before is not None and shares_new is not None:
        shares_after = args.shares_before + shares_new

    eps_current = safe_div(args.net_income_current, args.shares_before)
    eps_forward = safe_div(args.net_income_forward, shares_after)

    checks = []
    if pre is not None and post is not None and inv is not None:
        delta = abs((pre + inv) - post)
        tolerance = max(1.0, abs(post)) * 1e-9
        if delta > tolerance:
            checks.append("pre_money_plus_investment_does_not_equal_post_money")
    if own is not None and not (0 < own < 1):
        checks.append("investor_ownership_out_of_range")

    out = {
        "pre_money": pre,
        "investment": inv,
        "post_money": post,
        "investor_ownership": own,
        "shares_before": args.shares_before,
        "shares_new": shares_new,
        "shares_after": shares_after,
        "eps_current": eps_current,
        "eps_forward": eps_forward,
        "checks": checks,
    }
    print(json.dumps(out, ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()
