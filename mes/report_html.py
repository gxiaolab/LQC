import re


def html_add_readstat_table(html_string, readstat_table):
    rowstring_list = list()
    for ri, row in readstat_table.iterrows():
        tmprow_list = [
            '<th scope="row">{}</th>'.format(row['label']),
            '<td>{}</td>'.format(row['read_count']),
            '<td>{}</td>'.format(row['total_base']),
            '<td>{:.4}</td>'.format(row['read_length_mean']),
            '<td>{}</td>'.format(row['read_length_median']),
            '<td>{}</td>'.format(row['read_length_N50']),
            '<td>{}</td>'.format(row['read_length_L50'])
        ]
        if row['label'] == "Total":
            rowstring_list.append(
                '<tr class="table-secondary">' +
                '\n'.join(tmprow_list) + "</tr>"

            )
            total_read_count = row['read_count']
            total_base = row['total_base']
            total_median_read_length = row['read_length_median']
            total_mean_read_length = row['read_length_mean']
            total_N50 = row['read_length_N50']
            total_L50 = row['read_length_L50']
        else:
            rowstring_list.append(
                "<tr>" +
                '\n'.join(tmprow_list) + "</tr>"
            )

    new_html_string = re.sub(
        "\{%readstat_total_read_count%\}",
        '{}'.format(total_read_count), html_string
    )
    new_html_string = re.sub(
        "\{%readstat_total_base%\}",
        '{}'.format(total_base), new_html_string
    )
    new_html_string = re.sub(
        "\{%readstat_median_read_length%\}",
        '{}'.format(total_median_read_length),
        new_html_string
    )
    new_html_string = re.sub(
        "\{%readstat_mean_read_length%\}",
        '{:.4}'.format(total_mean_read_length),
        new_html_string
    )
    new_html_string = re.sub(
        "\{%readstat_N50%\}",
        '{}'.format(total_N50),
        new_html_string
    )
    new_html_string = re.sub(
        "\{%readstat_L50%\}",
        '{}'.format(total_L50),
        new_html_string
    )

    new_html_string = re.sub(
        "\{%readstat_table%\}",
        '\n'.join(rowstring_list), new_html_string
    )
    return new_html_string


def html_add_mismatch_table(html_string, mismatch_table,
                            mean_mismatch_per_read,
                            mismatch_type_counter):
    mis_types = ['a=>c', 'a=>g', 'a=>t', 'c=>a', 'c=>g', 'c=>t',
                 'g=>a', 'g=>c', 'g=>t', 't=>a', 't=>c', 't=>g']
    rowstring_list = list()
    for ri, row in mismatch_table.iterrows():
        tmprow_list = [
            '<th scope="row">{}</th>'.format(row['label'])
        ]
        for mis in mis_types:
            if mis in row:
                tmprow_list.append(
                    '<td>{}</td>'.format(row[mis]),
                )
            else:
                tmprow_list.append('<td>0</td>')
        if row['label'] == "Total":
            rowstring_list.append(
                '<tr class="table-secondary">' +
                '\n'.join(tmprow_list) + "</tr>"

            )
            total_mismatch_count = 0
            for idx in row.index:
                if idx != 'label':
                    total_mismatch_count += row[idx]
                else:
                    pass
        else:
            rowstring_list.append(
                "<tr>" +
                '\n'.join(tmprow_list) + "</tr>"
            )

    new_html_string = re.sub(
        "\{%mismatch_total_mismatch_number%\}",
        '{}'.format(total_mismatch_count),
        html_string
    )
    new_html_string = re.sub(
        "\{%mismatch_mean_mismatch_per_read%\}",
        '{:.4}'.format(mean_mismatch_per_read),
        new_html_string
    )
    mistype_list1 = list()
    for mis in mis_types[0:6]:
        mistype_list1.append(
            "<li>{}: {}</li>".format(
                mis, mismatch_type_counter[mis]
            )
        )
    mistype_list2 = list()
    for mis in mis_types[6:]:
        mistype_list2.append(
            "<li>{}: {}</li>".format(
                mis, mismatch_type_counter[mis]
            )
        )
    new_html_string = re.sub(
        "\{%mismatch_type_list1%\}",
        "<ul>" + '\n'.join(mistype_list1) + "</ul>",
        new_html_string
    )
    new_html_string = re.sub(
        "\{%mismatch_type_list2%\}",
        "<ul>" + '\n'.join(mistype_list2) + "</ul>",
        new_html_string
    )
    new_html_string = re.sub(
        "\{%mismatch_table%\}",
        '\n'.join(rowstring_list),
        new_html_string
    )
    return new_html_string


def html_add_insertion_table(html_string, insertion_table,
                             mean_insertion_per_read):
    rowstring_list = list()
    for ri, row in insertion_table.iterrows():
        tmprow_list = [
            '<th scope="row">{}</th>'.format(row['label']),
            '<td>{}</td>'.format(row['insertion_count']),
            '<td>{}</td>'.format(row['insertion_length']),
            '<td>{:.4}</td>'.format(row['mean_insertion_length']),
            '<td>{}</td>'.format(row['median_insertion_length'])
        ]
        if row['label'] == "Total":
            rowstring_list.append(
                '<tr class="table-secondary">' +
                '\n'.join(tmprow_list) + "</tr>"

            )
            total_insertion_count = row['insertion_count']
            total_insertion_length = row['insertion_length']
            mean_insertion_length = row['mean_insertion_length']
        else:
            rowstring_list.append(
                "<tr>" +
                '\n'.join(tmprow_list) + "</tr>"
            )

    new_html_string = re.sub(
        "\{%insertion_total_insertion_number%\}",
        '{}'.format(total_insertion_count),
        html_string
    )
    new_html_string = re.sub(
        "\{%insertion_total_insertion_length%\}",
        '{}'.format(total_insertion_length),
        new_html_string
    )
    new_html_string = re.sub(
        "\{%insertion_mean_insertion_length%\}",
        '{:.4}'.format(mean_insertion_length),
        new_html_string
    )
    new_html_string = re.sub(
        "\{%insertion_mean_insertion_per_read%\}",
        '{:.4}'.format(mean_insertion_per_read),
        new_html_string
    )
    new_html_string = re.sub(
        "\{%insertion_table%\}",
        '\n'.join(rowstring_list), new_html_string
    )
    return new_html_string


def html_add_deletion_table(html_string, deletion_table,
                            mean_deletion_per_read):
    rowstring_list = list()
    for ri, row in deletion_table.iterrows():
        tmprow_list = [
            '<th scope="row">{}</th>'.format(row['label']),
            '<td>{}</td>'.format(row['deletion_count']),
            '<td>{}</td>'.format(row['deletion_length']),
            '<td>{:.4}</td>'.format(row['mean_deletion_length']),
            '<td>{}</td>'.format(row['median_deletion_length'])
        ]
        if row['label'] == "Total":
            rowstring_list.append(
                '<tr class="table-secondary">' +
                '\n'.join(tmprow_list) + "</tr>"

            )
            total_deletion_count = row['deletion_count']
            total_deletion_length = row['deletion_length']
            mean_deletion_length = row['mean_deletion_length']
        else:
            rowstring_list.append(
                "<tr>" +
                '\n'.join(tmprow_list) + "</tr>"
            )

    new_html_string = re.sub(
        "\{%deletion_total_deletion_number%\}",
        '{}'.format(total_deletion_count),
        html_string
    )
    new_html_string = re.sub(
        "\{%deletion_total_deletion_length%\}",
        '{}'.format(total_deletion_length),
        new_html_string
    )
    new_html_string = re.sub(
        "\{%deletion_mean_deletion_length%\}",
        '{:.4}'.format(mean_deletion_length),
        new_html_string
    )
    new_html_string = re.sub(
        "\{%deletion_mean_deletion_per_read%\}",
        '{:.4}'.format(mean_deletion_per_read),
        new_html_string
    )
    new_html_string = re.sub(
        "\{%deletion_table%\}",
        '\n'.join(rowstring_list),
        new_html_string
    )
    return new_html_string


def html_add_splice_table(html_string, splice_table,
                          mean_intron_per_read):

    rowstring_list = list()
    for ri, row in splice_table.iterrows():
        label = ""
        gtag = 0
        gcag = 0
        atac = 0
        other = 0
        for rn in row.index:
            if rn == "label":
                label = row[rn]
            elif rn == "gt-ag":
                gtag = row[rn]
            elif rn == "gc-ag":
                gcag = row[rn]
            elif rn == "at-ac":
                atac = row[rn]
            else:
                other += row[rn]
        gtagp = gtag / sum([gtag, gcag, atac, other]) * 100
        gcagp = gcag / sum([gtag, gcag, atac, other]) * 100
        atacp = atac / sum([gtag, gcag, atac, other]) * 100
        otherp = other / sum([gtag, gcag, atac, other]) * 100
        tmprow_list = [
            '<th scope="row">{}</th>'.format(label),
            '<td>{}</td>'.format(gtag),
            '<td>{:.4}</td>'.format(gtagp),
            '<td>{}</td>'.format(gcag),
            '<td>{:.4}</td>'.format(gcagp),
            '<td>{}</td>'.format(atac),
            '<td>{:.4}</td>'.format(atacp),
            '<td>{}</td>'.format(other),
            '<td>{:.4}</td>'.format(otherp)
        ]
        if row['label'] == "Total":
            rowstring_list.append(
                '<tr class="table-secondary">' +
                '\n'.join(tmprow_list) + "</tr>"

            )
            total_gtag = gtag
            total_gtagp = gtagp
            total_gcag = gcag
            total_gcagp = gcagp
            total_atac = atac
            total_atacp = atacp
            total_other = other
            total_otherp = otherp
        else:
            rowstring_list.append(
                "<tr>" +
                '\n'.join(tmprow_list) + "</tr>"
            )

    splice_list = [
        "<li>gt-ag: {} ({:.4}%)</li>".format(
            total_gtag, total_gtagp
        ),
        "<li>gc-ag: {} ({:.4}%)</li>".format(
            total_gcag, total_gcagp
        ),
        "<li>at-ac: {} ({:.4}%)</li>".format(
            total_atac, total_atacp
        ),
        "<li>other: {} ({:.4}%)</li>".format(
            total_other, total_otherp
        )
    ]
    new_html_string = re.sub(
        "\{%splice_type_list%\}",
        "<ul>" + '\n'.join(splice_list) + "</ul>",
        html_string
    )
    new_html_string = re.sub(
        "\{%intron_total_intron_number%\}",
        '{}'.format(
            total_gtag + total_gcag +
            total_atac + total_other
        ),
        new_html_string
    )
    new_html_string = re.sub(
        "\{%intron_mean_intron_per_read%\}",
        '{:.4}'.format(mean_intron_per_read),
        new_html_string
    )
    new_html_string = re.sub(
        "\{%splice_table%\}",
        '\n'.join(rowstring_list),
        new_html_string
    )
    return new_html_string


########################################
